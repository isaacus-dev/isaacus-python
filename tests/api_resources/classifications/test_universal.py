# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from isaacus import Isaacus, AsyncIsaacus
from tests.utils import assert_matches_type
from isaacus.types.classifications import UniversalClassification

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUniversal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Isaacus) -> None:
        universal = client.classifications.universal.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
        )
        assert_matches_type(UniversalClassification, universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Isaacus) -> None:
        universal = client.classifications.universal.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
            chunking_options={
                "overlap_ratio": 0.1,
                "overlap_tokens": 0,
                "size": 512,
            },
            is_iql=True,
            scoring_method="auto",
        )
        assert_matches_type(UniversalClassification, universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Isaacus) -> None:
        response = client.classifications.universal.with_raw_response.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        universal = response.parse()
        assert_matches_type(UniversalClassification, universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Isaacus) -> None:
        with client.classifications.universal.with_streaming_response.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            universal = response.parse()
            assert_matches_type(UniversalClassification, universal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUniversal:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncIsaacus) -> None:
        universal = await async_client.classifications.universal.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
        )
        assert_matches_type(UniversalClassification, universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIsaacus) -> None:
        universal = await async_client.classifications.universal.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
            chunking_options={
                "overlap_ratio": 0.1,
                "overlap_tokens": 0,
                "size": 512,
            },
            is_iql=True,
            scoring_method="auto",
        )
        assert_matches_type(UniversalClassification, universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIsaacus) -> None:
        response = await async_client.classifications.universal.with_raw_response.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        universal = await response.parse()
        assert_matches_type(UniversalClassification, universal, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIsaacus) -> None:
        async with async_client.classifications.universal.with_streaming_response.create(
            model="kanon-universal-classifier",
            query="This is a confidentiality clause.",
            text="I agree not to tell anyone about the document.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            universal = await response.parse()
            assert_matches_type(UniversalClassification, universal, path=["response"])

        assert cast(Any, response.is_closed) is True
