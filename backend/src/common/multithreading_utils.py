import logging
import threading

from src.common.utils import delay_time

logger = logging.getLogger(__name__)


def make_thread(func, *args, **kwargs):
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.start()
    return thread


def add_task(
    func,
    *args,
    delay=None,
    **kwargs,
):
    def delayed_task():
        if delay:
            delay_time(delay)
        func(*args, **kwargs)

    make_thread(delayed_task)
