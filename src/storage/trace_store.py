from __future__ import annotations

from copy import deepcopy
from typing import Any, Literal, Protocol

from pydantic import BaseModel

StoreBackend = Literal["auto", "memory", "cosmos"]


class _TraceBackend(Protocol):
    def store(self, document: dict[str, Any]) -> None: ...

    def get(self, failure_id: str) -> dict[str, Any]: ...


class _InMemoryTraceBackend:
    def __init__(self) -> None:
        self._documents: dict[str, dict[str, Any]] = {}

    def store(self, document: dict[str, Any]) -> None:
        failure_id = str(document["failure_id"])
        self._documents[failure_id] = deepcopy(document)

    def get(self, failure_id: str) -> dict[str, Any]:
        if failure_id not in self._documents:
            raise KeyError(f"Trace '{failure_id}' not found.")

        return deepcopy(self._documents[failure_id])


class _CosmosTraceBackend:
    def __init__(self, client: Any) -> None:
        self._client = client

    def store(self, document: dict[str, Any]) -> None:
        self._client.upsert_trace_document(document)

    def get(self, failure_id: str) -> dict[str, Any]:
        return self._client.get_trace_document(failure_id)


def _coerce_payload(value: BaseModel | dict[str, Any]) -> dict[str, Any]:
    if isinstance(value, BaseModel):
        return value.model_dump()
    if isinstance(value, dict):
        return deepcopy(value)

    raise TypeError("TraceStore payloads must be dicts or pydantic models.")


def _cosmos_settings_available() -> bool:
    try:
        from src.storage.cosmos_client import load_cosmos_settings_from_env
    except ModuleNotFoundError:
        return False

    return load_cosmos_settings_from_env() is not None


def _create_cosmos_backend() -> _TraceBackend:
    try:
        from src.storage.cosmos_client import CosmosTraceClient
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Cosmos backend requires azure dependencies. Install requirements or use --store memory."
        ) from exc

    return _CosmosTraceBackend(CosmosTraceClient.from_env())


class TraceStore:
    def __init__(self, backend: StoreBackend = "auto") -> None:
        backend_name = backend
        if backend == "auto":
            backend_name = "cosmos" if _cosmos_settings_available() else "memory"

        if backend_name == "memory":
            self._backend: _TraceBackend = _InMemoryTraceBackend()
            self.backend_name = "memory"
            return

        if backend_name == "cosmos":
            self._backend = _create_cosmos_backend()
            self.backend_name = "cosmos"
            return

        raise ValueError(f"Unsupported backend '{backend}'.")

    def store_trace(
        self,
        failure_event: BaseModel | dict[str, Any],
        trace_record: BaseModel | dict[str, Any],
    ) -> None:
        failure_event_payload = _coerce_payload(failure_event)
        trace_record_payload = _coerce_payload(trace_record)

        failure_id = str(failure_event_payload.get("failure_id", "")).strip()
        trace_failure_id = str(trace_record_payload.get("failure_id", "")).strip()
        subject = str(failure_event_payload.get("subject", "")).strip()

        if not failure_id:
            raise ValueError("failure_event is missing 'failure_id'.")
        if failure_id != trace_failure_id:
            raise ValueError("failure_id mismatch between failure_event and trace_record.")
        if not subject:
            raise ValueError("failure_event is missing 'subject'.")

        document = {
            "id": failure_id,
            "failure_id": failure_id,
            "subject": subject,
            "failure_event": failure_event_payload,
            "trace_record": trace_record_payload,
        }
        self._backend.store(document)

    def get_trace(self, failure_id: str) -> dict[str, Any]:
        document = self._backend.get(failure_id)

        return {
            "failure_event": deepcopy(document["failure_event"]),
            "trace_record": deepcopy(document["trace_record"]),
        }
