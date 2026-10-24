# Flask + Redis Multi-Container Challenge: Step-by-Step Guide

## The big picture (read this first)

We're building a tiny website made of **3 containers** that work together:

| Container | What it is | Its job |
|---|---|---|
| **web** | A Python Flask app | Shows the web pages |
| **redis** | A Redis database | Remembers the visit count |
| **nginx** | A load balancer | Takes your browser's request and passes it to one of the web containers (needed for the scaling bonus) |

How a request travels:

```
Your browser  →  nginx (port 5000)  →  one of the web containers  →  redis
```

**Docker Compose** is the tool that starts all 3 containers together with one command.

---

## Step 0: Before you start (Mac only)

On a Mac, **port 5000 is already used by AirPlay Receiver**. If you skip this, `localhost:5000` won't show your app.

Fix it:
1. Open **System Settings**.
2. Go to **General → AirDrop & Handoff**.
3. Turn **AirPlay Receiver** off.

> Don't want to turn it off? You can use a different port instead. See the Troubleshooting section at the end.

Also make sure **Docker Desktop is open and running** (the whale icon at the top of the screen).

---

## Step 1: Create the folder structure

Make this folder layout. Each service gets its own folder:

```
flask-redis-app/
├── docker-compose.yml
├── web/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── redis/
│   └── Dockerfile
└── nginx/
    └── nginx.conf
```

In the terminal you can create all the folders at once:

```bash
mkdir -p flask-redis-app/web flask-redis-app/redis flask-redis-app/nginx
```

**What this does:** `mkdir` means "make directory" (a folder). `-p` lets it make several folders, and folders inside folders, in one go.

Then open the folder in VS Code:

```bash
code flask-redis-app
```

---

## Step 2: Write the Flask app (`web/app.py`)

```python
import os
import socket

from flask import Flask
import redis

app = Flask(__name__)

# Read the Redis connection details from environment variables.
# If they are not set, fall back to sensible defaults.
redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

db = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.route("/")
def welcome():
    return "Welcome to the Flask + Redis app!"


@app.route("/count")
def count():
    # INCR adds 1 to the "visits" key (and creates it if it doesn't exist yet)
    visits = db.incr("visits")
    # socket.gethostname() is the container's ID, so you can see which copy answered
    return f"This page has been visited {visits} times. (Served by container {socket.gethostname()})"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**Line-by-line, in plain English:**

- `import ...`: loads the tools we need. `flask` makes web pages, `redis` talks to the database, `os` reads environment variables and `socket` gets the container's name.
- `app = Flask(__name__)`: creates the web app.
- `os.environ.get("REDIS_HOST", "redis")`: "Look for a setting called `REDIS_HOST`. If there isn't one, use `redis`." This covers the **environment variables bonus**.
- `db = redis.Redis(...)`: connects to the Redis database. `decode_responses=True` makes Redis give back normal text instead of raw bytes.
- `@app.route("/")`: "When someone visits `/` (the home page), run the function below." It returns the welcome message.
- `@app.route("/count")`: "When someone visits `/count`, run this."
  - `db.incr("visits")`: tells Redis "add 1 to the number stored under the name `visits`." If it doesn't exist yet, Redis starts it at 0, so the first visit shows 1.
  - `socket.gethostname()`: the ID of the container that answered. It lets you **see the load balancing happen** in the bonus.
- `app.run(host="0.0.0.0", port=5000)`: starts the app on port 5000.
  - **Why `0.0.0.0`?** By default Flask only listens to requests from inside its own container. `0.0.0.0` means "accept requests from anywhere," so the other containers can reach it.

**Why is the host called `redis`?** Inside Docker Compose, containers find each other **by their service name**. Our database service is named `redis` in `docker-compose.yml`, so the Flask app can reach it at the address `redis`. It works like a phone contact name.

---

## Step 3: List the Python packages (`web/requirements.txt`)

```
flask==3.0.3
redis==5.0.8
```

**What this is:** a shopping list of Python packages for the container to install. The `==` numbers pin exact versions, so it works the same on every computer.

---

## Step 4: Dockerfile for the Flask app (`web/Dockerfile`)

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

A Dockerfile is a **recipe for building an image**. Line by line:

| Line | Meaning |
|---|---|
| `FROM python:3.12-slim` | Start from a small ready-made image that already has Python installed. |
| `WORKDIR /app` | Create a folder called `/app` inside the container and work from there. |
| `COPY requirements.txt .` | Copy the shopping list into the container. The `.` means "into the current folder" (`/app`). |
| `RUN pip install ...` | Install Flask and Redis. `--no-cache-dir` skips saving download files, which keeps the image smaller. |
| `COPY . .` | Copy the rest of your code (`app.py`) into the container. |
| `EXPOSE 5000` | A note saying "this app uses port 5000." |
| `CMD ["python", "app.py"]` | The command that runs when the container starts. |

**Why copy `requirements.txt` before the rest of the code?** Docker remembers (caches) each step. If you only change `app.py`, Docker reuses the saved "install packages" step instead of downloading everything again, so rebuilds are much faster.

---

## Step 5: Dockerfile for Redis (`redis/Dockerfile`)

```dockerfile
FROM redis:7-alpine

# --appendonly yes makes Redis save every change to disk (in /data)
CMD ["redis-server", "--appendonly", "yes"]
```

- `FROM redis:7-alpine`: starts from the official Redis image. `alpine` is a very small version of Linux, so the image stays tiny.
- `--appendonly yes`: by default Redis keeps most data in memory, which disappears when it stops. This setting makes Redis **write every change to a file** in the `/data` folder. Together with the volume in Step 7, this is the **persistent storage bonus**.

---

## Step 6: The load balancer config (`nginx/nginx.conf`)

This file is only needed for the **scaling bonus**.

```nginx
events {}

http {
    # Use Docker's built-in DNS so nginx finds every copy of the "web" service
    resolver 127.0.0.11 valid=10s;

    server {
        listen 80;

        location / {
            set $flask http://web:5000;
            proxy_pass $flask;
        }
    }
}
```

**Why do we need nginx?**
When you run 3 copies of the Flask app, they can't all claim port 5000 on your Mac. Only one thing can use a port at a time. So **nginx takes port 5000** and shares the visitors out between the copies. That's load balancing.

**What the lines mean:**
- `events {}`: a required section. Leaving it empty uses the defaults.
- `resolver 127.0.0.11`: this is Docker's built-in "phone book" (DNS). When nginx asks "where is `web`?", Docker answers with the addresses of all the web copies.
- `valid=10s`: check the phone book again every 10 seconds, so nginx notices if you add or remove copies.
- `listen 80`: nginx listens on port 80 inside its container.
- `proxy_pass`: forwards each request to `web:5000`, which means one of the Flask copies.
- `set $flask ...`: putting the address in a variable makes nginx look it up again over time, instead of only once at startup.

---

## Step 7: Tie it all together (`docker-compose.yml`)

Put this in the main `flask-redis-app` folder:

```yaml
services:
  web:
    build: ./web
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - redis

  redis:
    build: ./redis
    volumes:
      - redis-data:/data

  nginx:
    image: nginx:1.27-alpine
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    ports:
      - "${HOST_PORT:-5000}:80"
    depends_on:
      - web

volumes:
  redis-data:
```

> **Indentation matters in YAML.** Use spaces, not tabs, and keep the alignment exactly like above.

**What each part means:**

- `services:` is the list of containers to run.
- **web**
  - `build: ./web`: "Build this image using the Dockerfile in the `web` folder."
  - `environment:`: sets the environment variables that `app.py` reads, telling it where Redis lives. This is the **environment variables bonus**.
  - `depends_on: redis`: "Start Redis before the web app."
  - **Notice there's no `ports:` here.** That's on purpose: only nginx is reachable from your browser, so we can run several web copies without them fighting over a port.
- **redis**
  - `build: ./redis`: build using our Redis Dockerfile.
  - `volumes: redis-data:/data`: connects a Docker **volume** (a storage box that lives outside the container) to the `/data` folder where Redis saves its file. If you delete the container, the volume and your count are kept. This is the **persistent storage bonus**.
- **nginx**
  - `image: nginx:1.27-alpine`: uses the ready-made nginx image. There's no Dockerfile because we don't need to change it.
  - `volumes: ./nginx/nginx.conf:...:ro`: puts our config file inside the container. `ro` means read-only.
  - `ports: "${HOST_PORT:-5000}:80"`: connects **port 5000 on your Mac** to **port 80 inside nginx**. The `${HOST_PORT:-5000}` part means "use 5000 unless I say otherwise," which is handy if 5000 is taken.
- The `volumes:` section at the bottom creates the named storage box `redis-data`.

---

## Step 8: Build and start everything

In the terminal, go into the project folder:

```bash
cd flask-redis-app
```

Then build and start it all:

```bash
docker compose up -d --build
```

- `up`: start all the services.
- `--build`: build the images from your Dockerfiles first.
- `-d`: "detached," which runs everything in the background so you get your terminal back.

The first time takes a minute while Docker downloads Python, Redis and nginx.

Check that all 3 containers are running:

```bash
docker compose ps
```

You should see `web`, `redis` and `nginx`, each with the status **Up** or **running**.

---

## Step 9: Test the app

1. **Welcome page:** open `http://localhost:5000` in your browser.
   You should see: **Welcome to the Flask + Redis app!**
2. **Visit counter:** open `http://localhost:5000/count`.
   You should see: **This page has been visited 1 times.**
   Refresh the page and the number goes up by 1 each time. ✅

---

## Step 10 (Bonus): Scale to multiple Flask copies

Run 3 copies of the web app:

```bash
docker compose up -d --scale web=3
```

- `--scale web=3` means "run 3 copies of the `web` service."

Check with `docker compose ps`. You should now see `web-1`, `web-2` and `web-3`.

**See the load balancing happen:** refresh `http://localhost:5000/count` a few times and watch the **"Served by container ..."** ID at the end. It changes as nginx passes your visits to different copies. **The count still goes up correctly** because all copies share the same Redis database.

> If the ID doesn't change in the browser, the browser may be reusing one connection. Try this in the terminal instead, which makes a fresh request each time:
> ```bash
> for i in 1 2 3 4 5 6; do curl -s localhost:5000/count; echo; done
> ```

---

## Step 11 (Bonus): Prove the data is saved

1. Note the current count.
2. Stop and delete all the containers:
   ```bash
   docker compose down
   ```
3. Start them again:
   ```bash
   docker compose up -d
   ```
4. Visit `/count` again. The number **continues from where it was** instead of starting at 1. That's the volume doing its job. ✅

> ⚠️ `docker compose down -v` also deletes the volume, which **resets the count to zero**. Only use `-v` when you want a fresh start.

---

## Useful commands

| Command | What it does |
|---|---|
| `docker compose up -d --build` | Build and start everything |
| `docker compose ps` | Show which containers are running |
| `docker compose logs web` | Show the Flask app's messages (great for errors) |
| `docker compose up -d --scale web=3` | Run 3 Flask copies |
| `docker compose down` | Stop and remove the containers (keeps the data) |
| `docker compose down -v` | Stop, remove and **delete the saved data** |

---

## Troubleshooting

**`localhost:5000` shows nothing, or an error says the port is already in use**
AirPlay Receiver is still using port 5000 (see Step 0). Or run the app on port 5001 instead:
```bash
HOST_PORT=5001 docker compose up -d --build
```
Then use `http://localhost:5001` and `http://localhost:5001/count`.

**`/count` shows an error**
Check the Flask logs: `docker compose logs web`. A "connection refused" message usually means Redis hasn't started yet. Wait a few seconds and refresh.

**"Cannot connect to the Docker daemon"**
Docker Desktop isn't running. Open it and wait until the whale icon stops animating.

**I changed `app.py` but nothing changed**
Rebuild: `docker compose up -d --build`.

---

# Summary

## What was done

- Built a **Flask web app** with two pages:
  - `/` shows a welcome message.
  - `/count` adds 1 to a visit counter and shows it.
- Used **Redis** as the database that stores the visit count.
- Wrote a **Dockerfile for each service** (Flask and Redis).
- Used **Docker Compose** to start everything with one command.
- **All 3 bonuses:**
  - **Persistent storage:** the count survives restarts.
  - **Environment variables:** the Redis address isn't hard-coded in the app.
  - **Scaling + load balancing:** multiple Flask copies, with nginx sharing out the visits.

## How it was done

| Requirement | How |
|---|---|
| Two Flask routes | `@app.route("/")` and `@app.route("/count")` in `app.py` |
| Redis stores the count | `db.incr("visits")` adds 1 to a key called `visits` |
| Dockerize Flask | `web/Dockerfile` installs Python packages and runs `app.py` |
| Dockerize Redis | `redis/Dockerfile` uses the official Redis image with saving switched on |
| Docker Compose | `docker-compose.yml` defines the `web`, `redis` and `nginx` services |
| Persistent storage | Redis `--appendonly yes` + a `redis-data` volume mounted at `/data` |
| Environment variables | `REDIS_HOST` and `REDIS_PORT` set in Compose, read with `os.environ.get()` |
| Scaling | `docker compose up -d --scale web=3` |
| Load balancing | nginx listens on port 5000 and forwards requests to all `web` copies |

## Key ideas explained

- **Container:** a small, sealed box that holds an app and everything it needs to run.
- **Image:** the recipe result a container is created from. A Dockerfile builds an image.
- **Docker Compose:** runs several containers together from one file, like a conductor for an orchestra.
- **Service name = address:** in Compose, containers reach each other by service name (`redis`, `web`). No IP addresses are needed.
- **Redis:** a very fast "key-value" database. Think of a labelled jar: the label is `visits` and the contents are the number.
- **Volume:** storage that lives outside the container, so data isn't lost when the container is deleted.
- **Environment variable:** a setting passed to the app from outside. You can change the Redis address without editing any code.
- **Load balancer (nginx):** a receptionist who sends each visitor to whichever Flask copy is available.
- **Why the count stays correct when scaled:** every Flask copy talks to the **same** Redis, so they all share one counter.
