import os
import socket

from flask import Flask
import redis

app = Flask("flask-redis-compose")

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
