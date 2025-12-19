import time
from app.storage.redis_client import redis_client

WINDOW_SECONDS = 60

def update_features(event: dict):
    api_key = event["api_key"]
    base = f"api:{api_key}"

    # Requests per window
    redis_client.incr(f"{base}:count")
    redis_client.expire(f"{base}:count", WINDOW_SECONDS)

    # Unique endpoints
    redis_client.sadd(f"{base}:endpoints", event["path"])
    redis_client.expire(f"{base}:endpoints", WINDOW_SECONDS)

    # Unique IPs
    redis_client.sadd(f"{base}:ips", event["client_ip"])
    redis_client.expire(f"{base}:ips", WINDOW_SECONDS)
