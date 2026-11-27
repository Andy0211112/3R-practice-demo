"""Example module for the demo package"""

from .logger_config import logger


def hello_world(message):
    """Example function to say Hello world with a message"""
    logger.debug("This is DEBUG level log message")
    logger.info("This is INFO level log message")
    logger.warning("This is WARN level log message")
    logger.error("This is ERROR level log message")
    return f"Hello world!: {message}"

def prime_factorize(n: int) -> list[int]:
    """Return the prime factors of n in ascending order, e.g. 12 -> [2, 2, 3]."""
    if n < 2:
        raise ValueError("n must be an integer >= 2")

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:  # 剩下的部分本身就是質數
        factors.append(n)
    return factors