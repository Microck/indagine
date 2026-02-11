from __future__ import annotations

import pytest

from src.models.failure import FailureEvent
from src.models.trace_record import TraceRecord, TraceStep
from src.storage.trace_store import TraceStore


def _sample_payload(failure_id: str = "failure-123") -> tuple[FailureEvent, dict[str, object]]:
    failure_event = FailureEvent(
        failure_id=failure_id,
        subject="booking",
        failure_type="validation_error",
        timestamp="2026-02-11T00:00:00Z",
        trace_id="trace-123",
        error="date must match format",
        metadata={"status": "failed"},
    )
    trace_record = TraceRecord(
        failure_id=failure_id,
        subject="booking",
        status="failed",
        started_at="2026-02-11T00:00:00Z",
        ended_at="2026-02-11T00:00:01Z",
        steps=[
            TraceStep(
                name="subject_validation",
                kind="validation_error",
                input={"tool": "search_flights"},
                output=None,
                error="date must match format",
            )
        ],
    )
    return failure_event, trace_record.model_dump()


def test_trace_store_memory_roundtrip() -> None:
    store = TraceStore(backend="memory")
    failure_event, trace_record = _sample_payload()

    store.store_trace(failure_event, trace_record)
    recovered = store.get_trace("failure-123")

    assert recovered["failure_event"]["subject"] == "booking"
    assert recovered["trace_record"]["schema_version"] == 1
    assert recovered["trace_record"]["steps"][0]["kind"] == "validation_error"


def test_trace_store_memory_missing_failure_raises_key_error() -> None:
    store = TraceStore(backend="memory")

    with pytest.raises(KeyError):
        store.get_trace("missing")


def test_trace_store_auto_uses_memory_without_cosmos_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for env_var in ("COSMOS_ENDPOINT", "COSMOS_KEY", "COSMOS_DATABASE", "COSMOS_CONTAINER_TRACES"):
        monkeypatch.delenv(env_var, raising=False)

    store = TraceStore()

    assert store.backend_name == "memory"
