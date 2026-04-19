import random
from django.core.cache import cache

def fa2(user):
    code = str(random.randint(100000, 999999))
    cache.set(f"2fa_{user.id}", code, timeout=300)

    print("2FA CODE:", code)

    return code