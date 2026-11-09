# packaged_app: your product, one command

This folder is your product. It holds **one `docker-compose.yml`** that reuses the lab services you picked, the
service folders it builds, and **this README**, rewritten for your product (the part below the line). The owner of
`packaged_app/` keeps it working and leads the demo at the oral.

## How to build it (read, then delete this part)

1. **Start from a lab.** Copy `lab7/` (every module in one compose file, the Control Room included) or the lab of
   your main module into `packaged_app/`. Copy `world/` next to it, at the root of your repository, and
   `platform/hub/` if you keep the Control Room: the compose file reads them as `../world` and `../platform/hub`,
   so with this layout no path changes.
2. **Keep only what your product needs.** In `docker-compose.yml`, delete the service blocks you don't use (and
   their folders). Always delete `notebook` (the lab notebook is not part of a product) and `churn-cloud` (Thomas's
   demo). Delete any `depends_on:` line that names a service you removed, and in `hub` the `..._URL` lines of the
   modules you dropped (their panel then says "not built yet"). Delete the lab files you don't need either:
   `play.ipynb`, `nb_helpers.py`, `ANSWERS.md`, `PREP.md`, `MERGE.md`.
3. **One command, no flags.** If your product uses the chatbot, remove `profiles: [chat]` from `llm` and `talk` so
   they start with everything else, and say in the README that `sh get_model.sh` comes first (it downloads the
   1.1 GB model once). The command is then `docker compose up -d --build --wait`, or a `start.sh` that does it.
4. **Check the paths and the ports.** `docker compose config` (in `packaged_app/`) prints the whole file with every
   path resolved: it fails if a folder is missing. The ports the labs publish, all on `127.0.0.1` only:

   | Box | Port | Box | Port |
   | --- | --- | --- | --- |
   | hub (Control Room) | 8000 | find | 8006 |
   | churn | 8001 | legacy | 8010 |
   | route | 8002 | minio (S3 API, console) | 8020, 8021 |
   | notify | 8003 | postgres | 8040 |
   | orders | 8004 | llm | 8050 |
   | talk | 8005 | | |

   Keep a port only if the browser needs it: everything else stays private on the compose network,
   where the boxes call each other by name (`http://route:8002`). That is the public and private of your
   `ARCHITECTURE.md`.
5. **Test it the way it will be tested.** Clone your repository into a new folder, `cd packaged_app`, run your one command,
   open what your README says, try your three things, then `docker compose down -v`. Fix what failed, or write it
   down below.

**How it's tested.** You send the repository the day of the oral; it's run on another laptop (Docker Desktop, nothing else running): a fresh clone
of your repository, `cd packaged_app`, the one command of your README, the address it gives, the three things to
try, in that order. Nothing else is read to start it. A README that says honestly what doesn't work costs less
than a product that fails without warning.

---

# (Your product's name)

Group: ........   Owner of `packaged_app/`: ........   Modules: ........ (2 or 3)

(One sentence: who uses it, and for what.)

## Start it (one command)

```bash
cd packaged_app
docker compose up -d --build --wait
```

(If you use the chatbot: `sh get_model.sh` first, once.) It takes about ........ minutes the first time
(measured on ........).

## Open

- http://localhost:8000 (........)

## Three things to try

1. ........ (e.g. "ask the chat where order L-0117 is")
2. ........ (e.g. "stop route: `docker compose stop route`, and watch the queue in the Orders panel")
3. ........

## What doesn't work yet

- ........

## Stop it

```bash
docker compose down        # docker compose down -v also deletes the volumes
```
