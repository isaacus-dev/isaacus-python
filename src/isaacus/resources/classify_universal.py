# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import classify_universal_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.classify_universal_create_response import ClassifyUniversalCreateResponse

__all__ = ["ClassifyUniversalResource", "AsyncClassifyUniversalResource"]


class ClassifyUniversalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyUniversalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return ClassifyUniversalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyUniversalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/isaacus-python#with_streaming_response
        """
        return ClassifyUniversalResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: str,
        query: str,
        text: str,
        chunk: bool | NotGiven = NOT_GIVEN,
        chunk_overlap: Optional[float] | NotGiven = NOT_GIVEN,
        chunk_size: int | NotGiven = NOT_GIVEN,
        is_iql: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyUniversalCreateResponse:
        """
        Classify

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/classify/universal",
            body=maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "text": text,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "is_iql": is_iql,
                },
                classify_universal_create_params.ClassifyUniversalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyUniversalCreateResponse,
        )


class AsyncClassifyUniversalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyUniversalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyUniversalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyUniversalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/isaacus-python#with_streaming_response
        """
        return AsyncClassifyUniversalResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: str,
        query: str,
        text: str,
        chunk: bool | NotGiven = NOT_GIVEN,
        chunk_overlap: Optional[float] | NotGiven = NOT_GIVEN,
        chunk_size: int | NotGiven = NOT_GIVEN,
        is_iql: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyUniversalCreateResponse:
        """
        Classify

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/classify/universal",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "text": text,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "is_iql": is_iql,
                },
                classify_universal_create_params.ClassifyUniversalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyUniversalCreateResponse,
        )


class ClassifyUniversalResourceWithRawResponse:
    def __init__(self, classify_universal: ClassifyUniversalResource) -> None:
        self._classify_universal = classify_universal

        self.create = to_raw_response_wrapper(
            classify_universal.create,
        )


class AsyncClassifyUniversalResourceWithRawResponse:
    def __init__(self, classify_universal: AsyncClassifyUniversalResource) -> None:
        self._classify_universal = classify_universal

        self.create = async_to_raw_response_wrapper(
            classify_universal.create,
        )


class ClassifyUniversalResourceWithStreamingResponse:
    def __init__(self, classify_universal: ClassifyUniversalResource) -> None:
        self._classify_universal = classify_universal

        self.create = to_streamed_response_wrapper(
            classify_universal.create,
        )


class AsyncClassifyUniversalResourceWithStreamingResponse:
    def __init__(self, classify_universal: AsyncClassifyUniversalResource) -> None:
        self._classify_universal = classify_universal

        self.create = async_to_streamed_response_wrapper(
            classify_universal.create,
        )
