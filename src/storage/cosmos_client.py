from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

from azure.cosmos import CosmosClient, PartitionKey, exceptions


@dataclass(frozen=True)
class CosmosSettings:
    endpoint: str
    key: str
    database: str
    container_traces: str


def load_cosmos_settings_from_env() -> CosmosSettings | None:
    endpoint = os.getenv("COSMOS_ENDPOINT", "").strip()
    key = os.getenv("COSMOS_KEY", "").strip()
    database = os.getenv("COSMOS_DATABASE", "").strip()
    container_traces = os.getenv("COSMOS_CONTAINER_TRACES", "").strip()

    if not all((endpoint, key, database, container_traces)):
        return None

    return CosmosSettings(
        endpoint=endpoint,
        key=key,
        database=database,
        container_traces=container_traces,
    )


class CosmosTraceClient:
    def __init__(self, settings: CosmosSettings) -> None:
        self._settings = settings
        self._client = CosmosClient(url=settings.endpoint, credential=settings.key)
        database_client = self._client.create_database_if_not_exists(id=settings.database)
        self._container_client = database_client.create_container_if_not_exists(
            id=settings.container_traces,
            partition_key=PartitionKey(path="/failure_id"),
        )

    @classmethod
    def from_env(cls) -> CosmosTraceClient:
        settings = load_cosmos_settings_from_env()
        if settings is None:
            raise ValueError(
                "Missing Cosmos configuration. Set COSMOS_ENDPOINT, COSMOS_KEY, "
                "COSMOS_DATABASE, and COSMOS_CONTAINER_TRACES."
            )

        return cls(settings)

    def upsert_trace_document(self, document: dict[str, Any]) -> None:
        self._container_client.upsert_item(document)

    def get_trace_document(self, failure_id: str) -> dict[str, Any]:
        try:
            return self._container_client.read_item(item=failure_id, partition_key=failure_id)
        except exceptions.CosmosResourceNotFoundError as exc:
            raise KeyError(f"Trace '{failure_id}' not found.") from exc
