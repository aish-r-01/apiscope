import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class TrafficCaptureMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        event = {
            "api_key": request.headers.get("x-api-key", "anonymous"),
            "path": request.url.path,
            "method": request.method,
            "client_ip": request.client.host if request.client else "unknown",
            "status_code": response.status_code,
            "latency_ms": int((time.time() - start_time) * 1000),
        }

        # For now, just log it
        print(event)

        return response
