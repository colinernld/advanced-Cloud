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

### Module 1: ........

| What we measured | Before | After | Where and how | Date |
| --- | --- | --- | --- | --- |
| e.g. p95 of a profile lookup | 1,400 ms (empty store) | 4 ms (full store) | lab 1 notebook, section 3 | 6 Nov |
|  |  |  |  |  |

What surprised us: ........

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
