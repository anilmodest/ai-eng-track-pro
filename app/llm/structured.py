"""Ask for JSON, validate against a schema, repair once, then fail.
# STUB: removed for your route. Rebuild it: tests/weeks/test_week1.py says what it must do.
Time every call in a "model.call" span (app.trace.span), with add_usage and, from week 5, the
gen_ai.* attributes app.trace.set_attribute records (tests/weeks/test_week5.py names them).
"""

from pydantic import BaseModel

from app.llm.client import Message, ModelClient, ModelResponse


class SchemaError(Exception):
    """The model answered, twice, and neither answer fitted the schema."""

    def __init__(self, detail: str, raw: str) -> None:
        super().__init__(detail)
        self.detail = detail
        self.raw = raw


async def complete_structured[T: BaseModel](
    client: ModelClient,
    messages: list[Message],
    schema: type[T],
    *,
    attempts: int,
    base_delay_s: float,
    timeout_s: float,
) -> tuple[T, list[ModelResponse]]:
    """Return the parsed object and every response it took to get there."""
    raise NotImplementedError("complete_structured: build me (weeks/1/routes/pro.md)")
