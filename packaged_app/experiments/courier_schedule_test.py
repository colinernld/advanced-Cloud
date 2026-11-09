"""First test of the courier planner: does moving couriers to the evening cut late deliveries?

It runs the course simulation (world/sim.py) without the Control Room, with a chosen number of couriers on
duty per store and per hour, and compares two schedules on the same simulated days.

    python3 -I courier_schedule_test.py [path/to/world]

The world folder is, in order: the argument, the COURSE_WORLD variable, or ../../world (repo root).
The course files are only read. Late = delivered more than 30 minutes after the order.
Setup: 8 simulated days x 5 seeds per schedule (a seed = one random draw of who orders and when).
"""
import copy
import os
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORLD = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("COURSE_WORLD", HERE.parents[1] / "world"))
sys.path.insert(0, str(WORLD))
import sim as simmod  # noqa: E402  (the course simulation)

DAYS, SEEDS, STEP = 8, [1, 2, 3, 4, 5], 0.25
STORES = ("S1", "S2", "S3")


class Recording(simmod.Sim):
    """The simulation, plus one record per delivered order."""

    def __init__(self, *a, **kw):
        self.rec = []
        super().__init__(*a, **kw)

    def _event(self, o, kind, detail):
        if kind == "delivered":
            self.rec.append({"store": o["store"], "hour": int(o["placed_at"] // 60) % 24,
                             "took": o["delivered_at"] - o["placed_at"], "wait": o["picked_at"] - o["ready_at"]})
        super()._event(o, kind, detail)


def run(plan, seed):
    """plan(store, hour) -> number of couriers on duty. Couriers are cloned beyond the 10 of the course."""
    s = Recording(WORLD, seed=seed, warmup_min=0)
    by_store = defaultdict(list)
    for k in s.couriers:
        by_store[k["store"]].append(k)
    for st, ks in by_store.items():
        i = len(ks)
        while len(ks) < 25:
            i += 1
            c = copy.deepcopy(ks[len(ks) % 10])
            c["id"] = f"{st}-X{i}"
            ks.append(c)
    s.couriers = [k for ks in by_store.values() for k in ks]
    for k in s.couriers:
        k["state"] = "off"

    def go(minutes):
        hour = int(s.clock // 60) % 24
        for st, ks in by_store.items():
            n = plan(st, hour)
            for idx, k in enumerate(ks):
                if idx < n and k["state"] == "off":
                    k["state"] = "idle"
                elif idx >= n and k["state"] == "idle":
                    k["state"] = "off"
        s._advance(minutes)

    for _ in range(int(45 / STEP)):   # warm up, like the course does
        go(STEP)
    s.rec.clear()
    day0 = s.day_index
    while s.day_index - day0 < DAYS:
        go(STEP)
    return s.rec


def flat(a, b, c):
    n = {"S1": a, "S2": b, "S3": c}
    return lambda st, h: n[st]


def by_hour(off, peak):
    """off-peak staffing, and 18h-22h staffing, per store."""
    return lambda st, h: peak[st] if 18 <= h <= 22 else off[st]


PLANS = {"today (10/10/10)": flat(10, 10, 10),
         "ours (6/7/8, evening 12/15/18)": by_hour({"S1": 6, "S2": 7, "S3": 8}, {"S1": 12, "S2": 15, "S3": 18})}


def late_pct(recs):
    return 100 * sum(r["took"] > 30 for r in recs) / max(1, len(recs))


if __name__ == "__main__":
    results = {}
    for name, plan in PLANS.items():
        recs = []
        for seed in SEEDS:
            recs += run(plan, seed)
        results[name] = recs
        evening = [r for r in recs if 18 <= r["hour"] <= 21]
        print(f"{name:34s} orders={len(recs):6d}  late={late_pct(recs):5.1f}%  late 18-21h={late_pct(evening):5.1f}%")
    print("\nhour | couriers on duty (3 stores): today / ours | late%: today -> ours | wait for a courier, min")
    names = list(PLANS)
    for h in range(11, 24):
        on = [sum(PLANS[n](st, h) for st in STORES) for n in names]
        rows = [[r for r in results[n] if r["hour"] == h] for n in names]
        late = [late_pct(r) for r in rows]
        wait = [sum(x["wait"] for x in r) / max(1, len(r)) for r in rows]
        print(f"{h:02d}h | {on[0]:3d} / {on[1]:3d} | {late[0]:5.1f} -> {late[1]:5.1f} | {wait[0]:5.1f} -> {wait[1]:5.1f}")
    per_store = {st: late_pct([r for r in results[names[0]] if r["store"] == st]) for st in STORES}
    print("\nlate% per store, today's schedule:", {k: round(v, 1) for k, v in per_store.items()})
