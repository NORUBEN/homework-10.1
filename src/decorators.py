import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise
            finally:
                log_line = f"[{datetime.datetime.now().isoformat()}] {message}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_line + "\n")
                else:
                    print(log_line)

        return wrapper

    return decorator
