import logging
import re
import time

logger = logging.getLogger(__name__)


def delay_time(time_string="0.2s"):
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400, "y": 31536000}

    match = re.match(r"(\d+)([smhdy])", time_string)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        total_seconds = value * units[unit]
        time.sleep(total_seconds)
    else:
        logger.error("Invalid time string format: %s", time_string)
        time.sleep(0.2)
