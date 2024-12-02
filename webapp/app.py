from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

# Check if Redis is enabled
REDIS_ENABLED = os.getenv("REDIS_ENABLED", "false").lower() == "true"

if REDIS_ENABLED:
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, password=REDIS_PASSWORD)
else:
    redis_client = None


@app.route("/")
def index():
    if REDIS_ENABLED and redis_client:
        redis_client.set("message", "Hello from Redis!")
        message = redis_client.get("message")
    else:
        message = "Redis is disabled."
    return jsonify({"message": message})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
