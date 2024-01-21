import json
import logging
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from src.core.logger import LoggerSetup

logger_setup = LoggerSetup()
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        start_time = time.time()
        request_id = str(uuid.uuid4())
        request_time = time.time()

        request_body = await request.body()
        request_details = {
            "method": request.method,
            "path": request.url.path,
            "ip": request.client.host,
            "body": request_body.decode()
        }

        response = await call_next(request)
        process_time = time.time() - start_time
        response_time = time.time()
        response_body = b"".join([chunk async for chunk in response.body_iterator])
        response.body_iterator = AsyncIteratorWrapper([response_body])

        try:
            parsed_body = json.loads(response_body.decode())
        except json.JSONDecodeError:
            parsed_body = response_body.decode()

        response_details = {
            "status": "successful" if response.status_code < 400 else "failed",
            "status_code": response.status_code,
            "time_taken": f"{response_time - request_time:0.4f}s",
            "body": parsed_body
        }

        logger.info(json.dumps({
            "X-Process-Time": str(process_time),
            "X-API-REQUEST-ID": request_id,
            "request": request_details,
            "response": response_details
        }))

        return response


class AsyncIteratorWrapper:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value
