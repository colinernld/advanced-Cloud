# Business case (one page, send it Mon 16 Nov, before session 3)

Group: ........   Members: Ariane Boulet, Teo Desquatreveux, Coline Renauld

One page, short lines, not graded. Keep it at the root of your repository: it stays alive until the oral (the
session log at the bottom).

## The idea and its twist

**The courier planner.** Forecast orders per store and per hour, then decide how many couriers are on duty
in each dark store, hour by hour, for the next day.

- Modules (3): hourly order data (S2) · demand forecast (ML) · planner tested in the simulation (S3).
- Our twist: we do not only forecast, we **prove the planning pays**: the same simulation and the same orders,
  today's flat schedule against ours. And we stress it: what if the forecast is wrong by half?

## The pain (step 1)

- Today every store has 10 couriers all day. In the evening, orders wait for a free courier: in the
  simulation, **13% of deliveries are late overall and 27% between 18:00 and 21:00**, about 0% at lunch.
- The big store suffers most: with the same 10 couriers, **S3 is late 19% of the time, S1 only 5%**.
- A late delivery puts a customer at risk: in lab 1, Inès was a good customer until a delivery 28 minutes
  late and a complaint; the churn model now sees her "at risk".
- The decision that changes: how many couriers per store and per hour. Who decides: the operations manager,
  every evening for the next day. Today: the same number for everyone, all day.

## The KPIs (step 2)

Late = delivered more than 30 minutes after the order.

- **The number that proves it works:** share of late deliveries. Today **about 1 in 8** (13%), and
  **more than 1 in 4** in the evening (27%). Target: **fewer than 1 in 20** (under 5%), even in the evening.
- **The guardrail (we are not doing harm):** no hour gets worse than today. Watch out: the evening needs up to
  45 couriers on duty at once (today 30), so evening shifts. To check in the product.
- **How we show it moved:** the same simulation and the same orders twice, once with today's schedule and
  once with ours. First test already run, by hand (not a forecast yet):

| Schedule | Late deliveries | Late in the evening (18-21h) |
| --- | --- | --- |
| Today: 10 couriers per store, all day | 13% | 27% |
| Fewer in the afternoon, more in the evening | **2%** | **3%** |

Hour by hour, and where each number comes from: `docs/DECISIONS.md`, "Our numbers". One surprise: our hand
schedule is too thin at lunch (5-6% late), which a forecast per hour should fix. Hard question: what if the
forecast is wrong by half?

## The bricks you think you'll use (step 5)

| Brick (and its session) | Why you need it |
| --- | --- |
| Postgres, nightly pipeline, lake and warehouse (S2) | orders per store and per hour, copied every night |
| Data tests (S2) | a renamed field must not silently break the forecast |
| A forecast service, same shape as `churn` (S1) | numbers in, expected orders per store and hour out |
| The simulation and Control Room (S3 dashboard) | to run today's schedule against ours, and watch late % |

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
