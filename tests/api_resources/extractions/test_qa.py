# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from isaacus import Isaacus, AsyncIsaacus
from tests.utils import assert_matches_type
from isaacus.types.extractions import AnswerExtraction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQa:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Isaacus) -> None:
        qa = client.extractions.qa.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
        )
        assert_matches_type(AnswerExtraction, qa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Isaacus) -> None:
        qa = client.extractions.qa.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
            chunking_options={
                "overlap_ratio": 0.1,
                "overlap_tokens": 0,
                "size": 512,
            },
            ignore_inextractability=False,
            top_k=1,
        )
        assert_matches_type(AnswerExtraction, qa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Isaacus) -> None:
        response = client.extractions.qa.with_raw_response.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qa = response.parse()
        assert_matches_type(AnswerExtraction, qa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Isaacus) -> None:
        with client.extractions.qa.with_streaming_response.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qa = response.parse()
            assert_matches_type(AnswerExtraction, qa, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQa:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncIsaacus) -> None:
        qa = await async_client.extractions.qa.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
        )
        assert_matches_type(AnswerExtraction, qa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIsaacus) -> None:
        qa = await async_client.extractions.qa.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
            chunking_options={
                "overlap_ratio": 0.1,
                "overlap_tokens": 0,
                "size": 512,
            },
            ignore_inextractability=False,
            top_k=1,
        )
        assert_matches_type(AnswerExtraction, qa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIsaacus) -> None:
        response = await async_client.extractions.qa.with_raw_response.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qa = await response.parse()
        assert_matches_type(AnswerExtraction, qa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIsaacus) -> None:
        async with async_client.extractions.qa.with_streaming_response.create(
            model="kanon-answer-extractor",
            query="What is the punishment for murder in Victoria?",
            texts=[
                "The standard sentence for murder in the State of Victoria is 30 years if the person murdered was a police officer and 25 years in any other case."
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qa = await response.parse()
            assert_matches_type(AnswerExtraction, qa, path=["response"])

        assert cast(Any, response.is_closed) is True
