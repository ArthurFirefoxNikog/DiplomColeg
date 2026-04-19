from django.core.cache import cache
import time

def is_rate_limited(key, max_attempts, window):
    attempts = cache.get(key, [])

    now = time.time()

    attempts = [t for t in attempts if now - t < window]

    if len(attempts) >= max_attempts:
        return True

    attempts.append(now)
    cache.set(key, attempts, timeout=window)

    return False