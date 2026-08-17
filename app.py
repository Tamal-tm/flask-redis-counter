import os
from flask import Flask
import redis

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def index():
    count = r.incr("visits")
    return f"Hello! This page has been visited {count} times.\n"

@app.route("/healthz")
def healthz():
    try:
        r.ping()
        return {"status": "ok"}, 200
    except redis.exceptions.ConnectionError:
        return {"status": "redis unreachable"}, 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
