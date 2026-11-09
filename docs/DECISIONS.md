# Decisions

Owner: ........

Two parts: **our numbers** first (what you measured), then **one entry per decision** (why you chose it). The
decisions point at the numbers instead of repeating them. Your lab notebooks give you a start: each one prints your
numbers, and each one ends with one decision of yours.

A number counts only if you measured it and you say where (notebook cell, command, Control Room panel). A number
from a blog or an AI doesn't count.

---

## Our numbers

Start from the numbers your lab notebooks printed, then measure again on `packaged_app/`: they will not be the same,
and that is interesting. One table per module you picked.

### Module 1: courier planner (couriers on duty per store and per hour)

Before = today's schedule, 10 couriers per store all day. After = ours: 6/7/8 couriers per store, 12/15/18 from
18h to 22h. Where and how, for every line: `packaged_app/experiments/courier_schedule_test.py`, the course
simulation (`world/sim.py`) run without the Control Room, 8 simulated days x 5 seeds, about 21,000 orders per
schedule. Late = delivered more than 30 minutes after the order. Schedules set by hand, not by a forecast yet.

| What we measured | Before | After | Where and how | Date |
| --- | --- | --- | --- | --- |
| Late deliveries, all hours | 13.2% | 2.4% | script above, first lines of output | 9 Nov |
| Late deliveries, 18h to 21h | 27.5% | 2.9% | same | 9 Nov |
| Late deliveries at 20h | 40.0% | 3.1% | same, hour table | 9 Nov |
| Late deliveries at 12h and 13h | 0.3% and 0.4% | 4.5% and 6.0% | same, hour table | 9 Nov |
| Wait for a free courier at 20h | 10.6 min | 0.3 min | same, hour table | 9 Nov |
| Wait for a free courier at 11h | 0.1 min | 0.2 min | same, hour table | 9 Nov |
| Late deliveries per store (today's schedule) | S1 4.8%, S2 13.4%, S3 18.9% | not measured yet | same, last line | 9 Nov |
| Couriers on duty at the evening peak (3 stores) | 30 | 45 | the two schedules in the script | 9 Nov |

Hour by hour, couriers on duty (3 stores) and late deliveries, today -> ours:

| Hour | Couriers | Late | Hour | Couriers | Late |
| --- | --- | --- | --- | --- | --- |
| 11h | 30 -> 21 | 0.2% -> 0.0% | 18h | 30 -> 45 | 9.9% -> 2.9% |
| 12h | 30 -> 21 | 0.3% -> 4.5% | 19h | 30 -> 45 | 31.4% -> 2.9% |
| 13h | 30 -> 21 | 0.4% -> 6.0% | 20h | 30 -> 45 | 40.0% -> 3.1% |
| 14h | 30 -> 21 | 0.0% -> 1.2% | 21h | 30 -> 45 | 25.9% -> 2.8% |
| 15h | 30 -> 21 | 0.0% -> 0.0% | 22h | 30 -> 45 | 3.7% -> 0.2% |
| 16h | 30 -> 21 | 0.1% -> 0.1% | 23h | 30 -> 21 | 0.3% -> 0.0% |
| 17h | 30 -> 21 | 0.8% -> 1.5% |  |  |  |

What surprised us: the evening is the whole problem (up to 4 late deliveries in 10 at 20h, because orders wait
about 10 min for a courier), but our hand schedule is too thin at lunch (5-6% late at 12h and 13h, today 0%).
A forecast per hour should add couriers there. Also: it needs up to 45 couriers on duty at once in the evening,
more people than today's 30. Limits: a simulation made by the course, no courier shifts or breaks, no margin of
error computed.

### Module 2: ........

| What we measured | Before | After | Where and how | Date |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

What surprised us: ........

### The whole product

| What we measured | Value | Where and how | Date |
| --- | --- | --- | --- |
| memory of all boxes at rest (`docker stats`) |  |  |  |
| one request end to end (the main one of your product) |  |  |  |
| under a surge (Control Room Traffic panel, x5 or x20) |  |  |  |

Which box is the first to suffer, and how did you see it? ........

---

## The decisions

One entry per decision, newest at the bottom. At least one per module you picked. Same five headings every time,
3 to 6 lines each.

### D1 · (a title that says the choice, e.g. "The profile store saves itself with the append-only file")

Date and session: ........

**The decision.** What did you choose, in one sentence?

**The options we dropped.** At least two. For each: why not? (cost, speed, risk, effort)

**Our number.** Which line of "Our numbers" supports it? Before and after.

**What breaks first.** With this choice, what fails first, and which number or log line would show it?

**With ten times more customers.** What would you change, and what would it cost?

---

### D2 · ........
