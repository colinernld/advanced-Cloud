# Business case (one page, send it Mon 16 Nov, before session 3)

Group: ........   Members: ........, ........, ........, ........

One page, short lines, not graded. Keep it at the root of your repository: it stays alive until the oral (the
session log at the bottom).

## The idea and its twist

**The courier planner.** Forecast orders per store and per hour, then decide how many couriers are on duty
in each dark store, hour by hour, for the next day.

- Modules (3): hourly order data (S2) · demand forecast (ML) · planner tested in the simulation (S3).
- Our twist: we do not only forecast, we **prove the planning pays**. Same simulation, same orders, same
  courier-hours: today's flat schedule against ours. And we stress it: what if the forecast is wrong by half?

## The pain (step 1)

- Today every store has 10 couriers all day. In the evening the orders wait for a free courier.
  In the simulation (8 days, 5 seeds): **13% of deliveries are late overall, 27% between 18:00 and 21:00**,
  against about 0% at lunch. At 20:00 an order waits about **10 min** for a courier (0.1 min at lunch;
  first run, 3 seeds).
- The big store suffers most: with the same 10 couriers, **S3 is late 19% of the time, S1 only 5%**.
- A late delivery puts a customer at risk: in lab 1, Inès was a good customer until a delivery 28 minutes
  late and a complaint; the churn model now sees her "at risk".
- The decision that changes: how many couriers per store and per hour. Who decides: the operations manager,
  every evening for the next day. Today: the same number for everyone, all day.

## The KPIs (step 2)

Late = delivered more than 30 minutes after the order.

- **The number that proves it works:** share of late deliveries.
  Today **about 1 in 8** is late (13%), and **more than 1 in 4** between 18:00 and 21:00 (27%).
  Target: **fewer than 1 in 20** (under 5%), even in the evening.
- **The guardrail (we are not doing harm):** we do not add working hours: couriers are moved from the
  afternoon to the evening, not added. Watch out: the evening needs up to 45 couriers on duty at once
  (today 30), so it means evening shifts and more people on those hours. To check in the product.
- **How we show it moved:** the same simulation and the same orders twice, once with today's schedule and
  once with ours. Only the schedule changes. First test, already run.

| Schedule | Late deliveries | Late in the evening (18-21h) |
| --- | --- | --- |
| Today: 10 couriers per store, all day | 13% | 27% |
| Fewer in the afternoon, more in the evening | **2%** | **3%** |

Simple reading: the same couriers, but where the orders are. Late deliveries go from about 1 in 8 to
about 1 in 40.

Hour by hour, same two schedules (couriers on duty in the 3 stores together, and late deliveries):

| Hour | Couriers today | Couriers ours | Late today | Late ours |
| --- | --- | --- | --- | --- |
| 11h | 30 | 21 | 0% | 0% |
| 12h | 30 | 21 | 0% | **5%** |
| 13h | 30 | 21 | 0% | **6%** |
| 14h | 30 | 21 | 0% | 1% |
| 15h | 30 | 21 | 0% | 0% |
| 16h | 30 | 21 | 0% | 0% |
| 17h | 30 | 21 | 1% | 2% |
| 18h | 30 | 45 | 10% | 3% |
| 19h | 30 | 45 | 31% | 3% |
| 20h | 30 | 45 | 40% | 3% |
| 21h | 30 | 45 | 26% | 3% |
| 22h | 30 | 45 | 4% | 0% |
| 23h | 30 | 21 | 0% | 0% |

What it shows: the problem is the evening (18h to 21h), up to 4 late deliveries in 10 at 20h. Our schedule
fixes it, but it is too thin at lunch (12h and 13h: 5-6% late, today 0%). A forecast per hour should see the
lunch bump and add a few couriers there. That is the point of forecasting instead of guessing.

Careful: in this first test we set the schedules by hand, knowing the real evening peak. A real forecast will
do worse. Our hard question: what if the forecast is wrong by half? That is the number to measure next.

## The bricks you think you'll use (step 5)

| Brick (and its session) | Why you need it |
| --- | --- |
| Postgres, nightly pipeline, lake and warehouse (S2) | orders per store and per hour, copied every night |
| Data tests (S2) | a renamed field must not silently break the forecast |
| A forecast service, same shape as `churn` (S1) | numbers in, expected orders per store and hour out |
| The simulation and Control Room (S3 dashboard) | to run today's schedule against ours, and watch late % |
| A queue (S4), maybe | orders waiting for a courier are already a queue: to watch it, not to build |

## Who owns what

| Member | Part owned |
| --- | --- |
| ........ | `packaged_app/` |
| ........ | `docs/BUSINESS.md` |
| ........ | `docs/ARCHITECTURE.md` and `docs/CLOUD.md` |
| ........ | `docs/OPERATIONS.md` |

---

## Session log (three lines after each session)

What you learnt today that's worth bringing into your product · what to watch out for (what could break, cost
or age) · what you change in your plan, if anything.

| Session | Worth bringing in | To watch out for | What we change |
| --- | --- | --- | --- |
| S3 | | | |
| S4 | | | |
| S5 | | | |
| S6 | | | |
| S7 | | | |
| S8 | | | |
