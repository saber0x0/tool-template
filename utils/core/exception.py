import functools
from .logger import Logger
from .print import print_error


def exception(msg):
    def exception_decorator(func):
        def wrapper(*args, **kwargs):
            logger = Logger.get_instance().get_logger()
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                print_error("Interrupted...")
                return
            except:
                error = f"There was an exception in  {func.__name__}"
                logger.exception(error)
            if msg:
                print_error(msg)
        return wrapper
    return exception_decorator
