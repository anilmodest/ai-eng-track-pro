"""Retry with backoff, only for failures that retrying can fix.
# STUB: removed for your route. Rebuild it: tests/weeks/test_week1.py says what it must do.
"""

from collections.abc import Awaitable, Callable


async def with_timeout[T](call: Awaitable[T], seconds: float) -> T:
    """Await `call`, raising ModelTimeout if it takes longer than `seconds`."""
    raise NotImplementedError("with_timeout: build me (weeks/1/routes/pro.md)")


async def with_retry[T](
    make_call: Callable[[], Awaitable[T]],
    *,
    attempts: int,
    base_delay_s: float,
    timeout_s: float,
) -> T:
    """Run make_call() up to `attempts` times with backoff. Retry only ModelError.retryable."""
    raise NotImplementedError("with_retry: build me (weeks/1/routes/pro.md)")
