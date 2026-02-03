# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from isaacus import Isaacus, AsyncIsaacus
from tests.utils import assert_matches_type
from isaacus.types import EnrichmentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnrichments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Isaacus) -> None:
        enrichment = client.enrichments.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
        )
        assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Isaacus) -> None:
        enrichment = client.enrichments.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
            overflow_strategy=None,
        )
        assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Isaacus) -> None:
        response = client.enrichments.with_raw_response.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrichment = response.parse()
        assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Isaacus) -> None:
        with client.enrichments.with_streaming_response.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrichment = response.parse()
            assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnrichments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncIsaacus) -> None:
        enrichment = await async_client.enrichments.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
        )
        assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIsaacus) -> None:
        enrichment = await async_client.enrichments.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
            overflow_strategy=None,
        )
        assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIsaacus) -> None:
        response = await async_client.enrichments.with_raw_response.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrichment = await response.parse()
        assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIsaacus) -> None:
        async with async_client.enrichments.with_streaming_response.create(
            model="kanon-2-enricher-preview",
            texts=['1.5 You (the "User") agree to be bound by these Terms.'],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrichment = await response.parse()
            assert_matches_type(EnrichmentResponse, enrichment, path=["response"])

        assert cast(Any, response.is_closed) is True
