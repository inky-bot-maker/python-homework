import functools
import time


def retry(max_attempts: int = 3, delay: float = 1):
    if max_attempts < 1:
        raise ValueError("max_attempts must be >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Попытка {attempt} не удалась: {e!r}. Повтор через {delay} с")
                    time.sleep(delay)
        return wrapper
    return decorator


calls = {"count": 0}

@retry(max_attempts=3, delay=1)
def unstable():
    """Падает первые два раза, на третий срабатывает."""
    calls["count"] += 1
    if calls["count"] < 3:
        raise ConnectionError("сервер не отвечает")
    return "успех"

print(unstable())         
print(unstable.__name__)  
print(unstable.__doc__)   


@retry(max_attempts=2, delay=0.5)
def always_fails():
    raise ValueError("всегда ошибка")

try:
    always_fails()
except ValueError as e:
    print(f"Исключение проброшено: {e}")  