import logging
from statsd import StatsClient

from redash import settings

__version__ = '0.4.0'


def setup_logging():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s][PID:%(process)d][%(levelname)s][%(name)s] %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(settings.LOG_LEVEL)


setup_logging()
statsd_client = StatsClient(host=settings.STATSD_HOST, port=settings.STATSD_PORT, prefix=settings.STATSD_PREFIX)