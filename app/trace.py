"""Tracing: each request is a tree of spans (duration, tokens, cost, error).
# STUB: removed for your route. Every name below is used by the service; make each one do its job.
tests/weeks/test_week5.py says what a trace must contain. Week 5, Area 9: instrument it yourself.
"""

import uuid
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import datetime
from enum import StrEnum

from sqlmodel import Field, Session, SQLModel


class ErrorKind(StrEnum):
    provider_timeout = "provider_timeout"
    provider_error = "provider_error"
    schema_error = "schema_error"
    retrieval_empty = "retrieval_empty"
    guard_blocked = "guard_blocked"
    budget_exceeded = "budget_exceeded"
    kill_switch = "kill_switch"
    not_found = "not_found"
    unsupported = "unsupported"
    unknown = "unknown"


class Span(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    request_id: str = Field(index=True)
    name: str = Field(index=True)
    parent: str | None = None
    started_at: datetime
    duration_ms: int = 0
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0
    error_kind: str | None = None
    detail: str = ""
    attributes: str = "{}"  # JSON: OpenTelemetry-style key/value pairs


def begin_request(name: str) -> str:
    """Start a request root; return the request id (sent back as X-Request-Id)."""
    return uuid.uuid4().hex[:12]  # TODO: open the root span and remember it for this request


def current_request_id() -> str | None:
    return None  # TODO


def mark_error(kind: ErrorKind | str, detail: str = "") -> None:
    """Record why the current request failed, on the innermost open span and the root."""
    return None  # TODO


def note(text: str) -> None:
    """Leave a short note on the request root (what was asked, what was answered)."""
    return None  # TODO


def set_attribute(key: str, value: str | int | float | bool) -> None:
    """Set an OpenTelemetry-style attribute (gen_ai.request.model, ...) on the innermost span."""
    return None  # TODO: stored with the span as JSON in Span.attributes


def add_usage(tokens_in: int, tokens_out: int, cost_usd: float) -> None:
    """Attribute tokens and cost to the innermost open span AND roll them up to the root."""
    return None  # TODO


@asynccontextmanager
async def span(name: str) -> AsyncIterator[None]:
    """Time a step under the current request. No-op outside a request."""
    yield  # TODO: record start, end, parent, and an error kind if the body raises


def end_request(session: Session) -> list[Span]:
    """Close the root, persist every span of this request, clear the context."""
    return []  # TODO


def spans_for(session: Session, request_id: str) -> list[Span]:
    return []  # TODO: every span of that request, in order


def recent_roots(session: Session, limit: int = 20) -> list[Span]:
    return []  # TODO: newest request roots first


def spent_since(session: Session, since: datetime) -> float:
    """Total attributed model cost across request roots since `since` (the budget's input)."""
    return 0.0  # TODO
