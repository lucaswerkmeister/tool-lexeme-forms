import logging
from gunicorn import glogging

class CustomGunicornLogger(glogging.Logger):
    """See <https://stackoverflow.com/a/59393519/1420237>."""

    def setup(self, cfg):
        super().setup(cfg)

        # Add filters to Gunicorn logger
        logger = logging.getLogger("gunicorn.access")
        logger.addFilter(HealthCheckFilter())

class HealthCheckFilter(logging.Filter):
    def filter(self, record):
        return 'GET /healthz' not in record.getMessage()

# send access log to stdout
accesslog = '-'
# (except /healthz which gets many requests from Kubernetes startup and liveness probes)
logger_class = CustomGunicornLogger

# allow long request URLs, we can have many &form_representation= params
limit_request_line = 8190

# 4 worker processes (not to be confused with `threads`)
workers = 4

# from app import app
wsgi_app = 'app:app'
