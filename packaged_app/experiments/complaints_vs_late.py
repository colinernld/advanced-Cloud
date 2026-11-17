"""Why a late delivery matters: complaints and late orders in the course's history file.

    python3 -I complaints_vs_late.py [path/to/world]

Reads world/data/customers.json (synthetic, 2,000 customers, 33,364 orders, 1,112 complaints). Read only.
Late = delivered more than 30 minutes after the order (promised 30 min). The world folder is, in order: the
argument, the COURSE_WORLD variable, or ../../world (repo root).
"""
import json
import os
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORLD = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("COURSE_WORLD", HERE.parents[1] / "world"))
data = json.loads((WORLD / "data" / "customers.json").read_text())

orders = {o[0]: o for c in data["customers"] for o in c["orders"]}   # [id, placed, total EUR, items, promised, took]
tickets = [t for c in data["customers"] for t in c["tickets"]]       # [id, order id, opened, reason]
late = lambda o: o[5] > o[4]  # noqa: E731
late_orders = [o for o in orders.values() if late(o)]
complained = {t[1] for t in tickets}
late_tickets = [t for t in tickets if t[3] == "late delivery"]

print(f"orders: {len(orders)}  average basket: {sum(o[2] for o in orders.values()) / len(orders):.1f} EUR")
print(f"late orders: {len(late_orders)} ({100 * len(late_orders) / len(orders):.1f}%)")
print(f"complaints: {len(tickets)}  by reason: {Counter(t[3] for t in tickets).most_common()}")
print(f"'late delivery' complaints on an order really late: {sum(late(orders[t[1]]) for t in late_tickets)} of {len(late_tickets)}")
on_time = len(orders) - len(late_orders)
print(f"complaint rate, late orders: {100 * sum(o[0] in complained for o in late_orders) / len(late_orders):.1f}%")
print(f"complaint rate, on-time orders: {100 * sum(o[0] in complained for o in orders.values() if not late(o)) / on_time:.1f}%")
