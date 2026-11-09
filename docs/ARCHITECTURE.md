# Architecture (on localhost)

Owner: ........   Group: ........   Modules picked: ........ (2 or 3)

## The product in two sentences

- Who uses it, and for what? What does it do that one module alone doesn't?

## The functional view (step 3)

The steps in business words, no technology names.

| Step | Who starts it | Data it needs | How fresh |
| --- | --- | --- | --- |
| ........ | | | |

## The system view (high level)

Your services and how they talk to each other: one box per service, one arrow per call or event, labelled
(an API call, an event, a nightly job). Excalidraw recommended: keep the `.excalidraw` file and a PNG export in
`docs/`.

## The detailed architecture (low level)

The full Popote map with everything you add, box by box. On it, mark:

- the **load balancer** in front of any service you run several copies of, and how copies share (or don't
  share) state;
- the **orchestrator** and its steps if you have pipelines, with their schedule and what each step waits for;
- queues, stores and where each piece of data lives (memory, a volume, a database, a bucket, the lake);
- which boxes are **public** (a published port, a public URL in the cloud) and which stay **private** (called
  by name on the compose network);
- for every arrow: pulled or pushed, and what happens if it's lost or arrives twice.

## Box by box

One short paragraph per box:

- What does it do, and which module of the course does it come from?
- Whom does it call, and who calls it (which route, which contract in `CONTRACTS.md`)?
- What does it keep, and does that survive a restart? A `docker compose down -v`?
- **What happens when it is down?** What does the customer see, and which other box suffers first?

## How to start it

- The one command and what to open are in `packaged_app/README.md`: say here which boxes it starts, on which ports.
- What you know does not work yet.
