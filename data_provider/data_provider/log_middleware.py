import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request received: {request.method} {request.get_full_path()} from {request.META['REMOTE_ADDR']}")
        response = self.get_response(request)
        return response