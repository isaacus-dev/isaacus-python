# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import reranking_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.reranking import Reranking

__all__ = ["RerankingsResource", "AsyncRerankingsResource"]


class RerankingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RerankingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return RerankingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RerankingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return RerankingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["kanon-universal-classifier", "kanon-universal-classifier-mini"],
        query: str,
        texts: List[str],
        chunking_options: Optional[reranking_create_params.ChunkingOptions] | NotGiven = NOT_GIVEN,
        is_iql: bool | NotGiven = NOT_GIVEN,
        scoring_method: Literal["auto", "chunk_max", "chunk_avg", "chunk_min"] | NotGiven = NOT_GIVEN,
        top_n: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Reranking:
        """
        Rerank legal documents by their relevance to a query with an Isaacus legal AI
        reranker.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#reranking) to use for
              reranking.

          query: The query to evaluate the relevance of the texts to.

              The query must contain at least one non-whitespace character.

              Unlike the texts being reranked, the query cannot be so long that it exceeds the
              maximum input length of the reranker.

          texts: The texts to rerank.

              There must be at least one text.

              Each text must contain at least one non-whitespace character.

          chunking_options: Options for how to split text into smaller chunks.

          is_iql: Whether the query should be interpreted as an
              [Isaacus Query Language (IQL)](https://docs.isaacus.com/iql) query, which is not
              the case by default.

              If you allow untrusted users to construct their own queries, think carefully
              before enabling IQL since queries can be crafted to consume an excessively large
              amount of tokens.

          scoring_method: The method to use for producing an overall relevance score for a text.

              `auto` is the default scoring method and is recommended for most use cases.
              Currently, it is equivalent to `chunk_max`. In the future, it will automatically
              select the best method based on the model and inputs.

              `chunk_max` uses the highest relevance score of all of a text's chunks.

              `chunk_avg` averages the relevance scores of all of a text's chunks.

              `chunk_min` uses the lowest relevance score of all of a text's chunks.

          top_n: A whole number greater than or equal to 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/rerankings",
            body=maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "texts": texts,
                    "chunking_options": chunking_options,
                    "is_iql": is_iql,
                    "scoring_method": scoring_method,
                    "top_n": top_n,
                },
                reranking_create_params.RerankingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reranking,
        )


class AsyncRerankingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRerankingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRerankingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRerankingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return AsyncRerankingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["kanon-universal-classifier", "kanon-universal-classifier-mini"],
        query: str,
        texts: List[str],
        chunking_options: Optional[reranking_create_params.ChunkingOptions] | NotGiven = NOT_GIVEN,
        is_iql: bool | NotGiven = NOT_GIVEN,
        scoring_method: Literal["auto", "chunk_max", "chunk_avg", "chunk_min"] | NotGiven = NOT_GIVEN,
        top_n: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Reranking:
        """
        Rerank legal documents by their relevance to a query with an Isaacus legal AI
        reranker.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#reranking) to use for
              reranking.

          query: The query to evaluate the relevance of the texts to.

              The query must contain at least one non-whitespace character.

              Unlike the texts being reranked, the query cannot be so long that it exceeds the
              maximum input length of the reranker.

          texts: The texts to rerank.

              There must be at least one text.

              Each text must contain at least one non-whitespace character.

          chunking_options: Options for how to split text into smaller chunks.

          is_iql: Whether the query should be interpreted as an
              [Isaacus Query Language (IQL)](https://docs.isaacus.com/iql) query, which is not
              the case by default.

              If you allow untrusted users to construct their own queries, think carefully
              before enabling IQL since queries can be crafted to consume an excessively large
              amount of tokens.

          scoring_method: The method to use for producing an overall relevance score for a text.

              `auto` is the default scoring method and is recommended for most use cases.
              Currently, it is equivalent to `chunk_max`. In the future, it will automatically
              select the best method based on the model and inputs.

              `chunk_max` uses the highest relevance score of all of a text's chunks.

              `chunk_avg` averages the relevance scores of all of a text's chunks.

              `chunk_min` uses the lowest relevance score of all of a text's chunks.

          top_n: A whole number greater than or equal to 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/rerankings",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "texts": texts,
                    "chunking_options": chunking_options,
                    "is_iql": is_iql,
                    "scoring_method": scoring_method,
                    "top_n": top_n,
                },
                reranking_create_params.RerankingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reranking,
        )


class RerankingsResourceWithRawResponse:
    def __init__(self, rerankings: RerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = to_raw_response_wrapper(
            rerankings.create,
        )


class AsyncRerankingsResourceWithRawResponse:
    def __init__(self, rerankings: AsyncRerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = async_to_raw_response_wrapper(
            rerankings.create,
        )


class RerankingsResourceWithStreamingResponse:
    def __init__(self, rerankings: RerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = to_streamed_response_wrapper(
            rerankings.create,
        )


class AsyncRerankingsResourceWithStreamingResponse:
    def __init__(self, rerankings: AsyncRerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = async_to_streamed_response_wrapper(
            rerankings.create,
        )
