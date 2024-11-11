from functools import wraps

from utils.log_funcs import log_error


def log_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_error(f"Error in {func.__name__}: {e}")
            return None

    return wrapper
