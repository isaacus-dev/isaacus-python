# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.classifications import universal_create_params
from ...types.classifications.universal_classification import UniversalClassification

__all__ = ["UniversalResource", "AsyncUniversalResource"]


class UniversalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UniversalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return UniversalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UniversalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return UniversalResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["kanon-universal-classifier", "kanon-universal-classifier-mini"],
        query: str,
        text: str,
        chunking_options: Optional[universal_create_params.ChunkingOptions] | NotGiven = NOT_GIVEN,
        is_iql: bool | NotGiven = NOT_GIVEN,
        scoring_method: Literal["auto", "chunk_max", "chunk_avg", "chunk_min"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UniversalClassification:
        """
        Classify the relevance of a legal document to a query using an Isaacus universal
        legal AI classifier.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#universal-classification)
              to use for universal classification.

          query: The [Isaacus Query Language (IQL)](https://docs.isaacus.com/iql) query or, if
              IQL is disabled, the statement, to evaluate the text against.

              The query must contain at least one non-whitespace character.

              Unlike the text being classified, the query cannot be so long that it exceeds
              the maximum input length of the universal classifier.

          text: The text to classify.

              The text must contain at least one non-whitespace character.

          chunking_options: Options for how to split text into smaller chunks.

          is_iql: Whether the query should be interpreted as an
              [IQL](https://docs.isaacus.com/iql) query or else as a statement.

          scoring_method: The method to use for producing an overall confidence score.

              `auto` is the default scoring method and is recommended for most use cases.
              Currently, it is equivalent to `chunk_max`. In the future, it will automatically
              select the best method based on the model and input.

              `chunk_max` uses the highest confidence score of all of the text's chunks.

              `chunk_avg` averages the confidence scores of all of the text's chunks.

              `chunk_min` uses the lowest confidence score of all of the text's chunks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/classifications/universal",
            body=maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "text": text,
                    "chunking_options": chunking_options,
                    "is_iql": is_iql,
                    "scoring_method": scoring_method,
                },
                universal_create_params.UniversalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UniversalClassification,
        )


class AsyncUniversalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUniversalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUniversalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUniversalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return AsyncUniversalResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["kanon-universal-classifier", "kanon-universal-classifier-mini"],
        query: str,
        text: str,
        chunking_options: Optional[universal_create_params.ChunkingOptions] | NotGiven = NOT_GIVEN,
        is_iql: bool | NotGiven = NOT_GIVEN,
        scoring_method: Literal["auto", "chunk_max", "chunk_avg", "chunk_min"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UniversalClassification:
        """
        Classify the relevance of a legal document to a query using an Isaacus universal
        legal AI classifier.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#universal-classification)
              to use for universal classification.

          query: The [Isaacus Query Language (IQL)](https://docs.isaacus.com/iql) query or, if
              IQL is disabled, the statement, to evaluate the text against.

              The query must contain at least one non-whitespace character.

              Unlike the text being classified, the query cannot be so long that it exceeds
              the maximum input length of the universal classifier.

          text: The text to classify.

              The text must contain at least one non-whitespace character.

          chunking_options: Options for how to split text into smaller chunks.

          is_iql: Whether the query should be interpreted as an
              [IQL](https://docs.isaacus.com/iql) query or else as a statement.

          scoring_method: The method to use for producing an overall confidence score.

              `auto` is the default scoring method and is recommended for most use cases.
              Currently, it is equivalent to `chunk_max`. In the future, it will automatically
              select the best method based on the model and input.

              `chunk_max` uses the highest confidence score of all of the text's chunks.

              `chunk_avg` averages the confidence scores of all of the text's chunks.

              `chunk_min` uses the lowest confidence score of all of the text's chunks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/classifications/universal",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "text": text,
                    "chunking_options": chunking_options,
                    "is_iql": is_iql,
                    "scoring_method": scoring_method,
                },
                universal_create_params.UniversalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UniversalClassification,
        )


class UniversalResourceWithRawResponse:
    def __init__(self, universal: UniversalResource) -> None:
        self._universal = universal

        self.create = to_raw_response_wrapper(
            universal.create,
        )


class AsyncUniversalResourceWithRawResponse:
    def __init__(self, universal: AsyncUniversalResource) -> None:
        self._universal = universal

        self.create = async_to_raw_response_wrapper(
            universal.create,
        )


class UniversalResourceWithStreamingResponse:
    def __init__(self, universal: UniversalResource) -> None:
        self._universal = universal

        self.create = to_streamed_response_wrapper(
            universal.create,
        )


class AsyncUniversalResourceWithStreamingResponse:
    def __init__(self, universal: AsyncUniversalResource) -> None:
        self._universal = universal

        self.create = async_to_streamed_response_wrapper(
            universal.create,
        )
