# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from isaacus import Isaacus, AsyncIsaacus
from tests.utils import assert_matches_type
from isaacus.types import Reranking

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRerankings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Isaacus) -> None:
        reranking = client.rerankings.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
        )
        assert_matches_type(Reranking, reranking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Isaacus) -> None:
        reranking = client.rerankings.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
            chunking_options={
                "overlap_ratio": 0.1,
                "overlap_tokens": 0,
                "size": 512,
            },
            is_iql=False,
            scoring_method="auto",
            top_n=1,
        )
        assert_matches_type(Reranking, reranking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Isaacus) -> None:
        response = client.rerankings.with_raw_response.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = response.parse()
        assert_matches_type(Reranking, reranking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Isaacus) -> None:
        with client.rerankings.with_streaming_response.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = response.parse()
            assert_matches_type(Reranking, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRerankings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncIsaacus) -> None:
        reranking = await async_client.rerankings.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
        )
        assert_matches_type(Reranking, reranking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIsaacus) -> None:
        reranking = await async_client.rerankings.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
            chunking_options={
                "overlap_ratio": 0.1,
                "overlap_tokens": 0,
                "size": 512,
            },
            is_iql=False,
            scoring_method="auto",
            top_n=1,
        )
        assert_matches_type(Reranking, reranking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIsaacus) -> None:
        response = await async_client.rerankings.with_raw_response.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = await response.parse()
        assert_matches_type(Reranking, reranking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIsaacus) -> None:
        async with async_client.rerankings.with_streaming_response.create(
            model="kanon-universal-classifier",
            query="What are the essential elements required to establish a negligence claim?",
            texts=[
                "To form a contract, there must be an offer, acceptance, consideration, and mutual intent to be bound.",
                "Criminal cases involve a completely different standard, requiring proof beyond a reasonable doubt.",
                "In a negligence claim, the plaintiff must prove duty, breach, causation, and damages.",
                "Negligence in tort law requires establishing a duty of care that the defendant owed to the plaintiff.",
                "The concept of negligence is central to tort law, with courts assessing whether a breach of duty caused harm.",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = await response.parse()
            assert_matches_type(Reranking, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True
