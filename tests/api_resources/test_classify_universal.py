# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from isaacus import Isaacus, AsyncIsaacus
from tests.utils import assert_matches_type
from isaacus.types import ClassifyUniversalCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassifyUniversal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Isaacus) -> None:
        classify_universal = client.classify_universal.create(
            model="model",
            query="query",
            text="text",
        )
        assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Isaacus) -> None:
        classify_universal = client.classify_universal.create(
            model="model",
            query="query",
            text="text",
            chunk=True,
            chunk_overlap=0,
            chunk_size=0,
            is_iql=True,
        )
        assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Isaacus) -> None:
        response = client.classify_universal.with_raw_response.create(
            model="model",
            query="query",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify_universal = response.parse()
        assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Isaacus) -> None:
        with client.classify_universal.with_streaming_response.create(
            model="model",
            query="query",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify_universal = response.parse()
            assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassifyUniversal:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncIsaacus) -> None:
        classify_universal = await async_client.classify_universal.create(
            model="model",
            query="query",
            text="text",
        )
        assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIsaacus) -> None:
        classify_universal = await async_client.classify_universal.create(
            model="model",
            query="query",
            text="text",
            chunk=True,
            chunk_overlap=0,
            chunk_size=0,
            is_iql=True,
        )
        assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIsaacus) -> None:
        response = await async_client.classify_universal.with_raw_response.create(
            model="model",
            query="query",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify_universal = await response.parse()
        assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIsaacus) -> None:
        async with async_client.classify_universal.with_streaming_response.create(
            model="model",
            query="query",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify_universal = await response.parse()
            assert_matches_type(ClassifyUniversalCreateResponse, classify_universal, path=["response"])

        assert cast(Any, response.is_closed) is True
