# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

from ..types import enrichment_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.enrichment_response import EnrichmentResponse

__all__ = ["EnrichmentsResource", "AsyncEnrichmentsResource"]


class EnrichmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnrichmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return EnrichmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrichmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return EnrichmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["kanon-2-enricher-preview"],
        texts: Union[SequenceNotStr[str], str],
        overflow_strategy: Optional[Literal["auto", "drop_end"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrichmentResponse:
        """
        Enrich documents with an Isaacus enricher model.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#enrichment) to use for
              enrichment.

          texts: A text or array of texts to be enriched, each containing at least one
              non-whitespace character.

              No more than 8 texts can be enriched in a single request.

          overflow_strategy: The strategy for handling content exceeding the model's maximum input length.

              `auto` currently behaves the same as `drop_end`, dropping excess tokens from the
              end of input. In the future, `auto` may implement more sophisticated strategies
              such as chunking and context-aware stitching.

              `drop_end` drops tokens from the end of input exceeding the model's maximum
              input length.

              `null`, which is the default setting, raises an error if the input exceeds the
              model's maximum input length.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/enrichments",
            body=maybe_transform(
                {
                    "model": model,
                    "texts": texts,
                    "overflow_strategy": overflow_strategy,
                },
                enrichment_create_params.EnrichmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrichmentResponse,
        )


class AsyncEnrichmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnrichmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrichmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrichmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return AsyncEnrichmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["kanon-2-enricher-preview"],
        texts: Union[SequenceNotStr[str], str],
        overflow_strategy: Optional[Literal["auto", "drop_end"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrichmentResponse:
        """
        Enrich documents with an Isaacus enricher model.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#enrichment) to use for
              enrichment.

          texts: A text or array of texts to be enriched, each containing at least one
              non-whitespace character.

              No more than 8 texts can be enriched in a single request.

          overflow_strategy: The strategy for handling content exceeding the model's maximum input length.

              `auto` currently behaves the same as `drop_end`, dropping excess tokens from the
              end of input. In the future, `auto` may implement more sophisticated strategies
              such as chunking and context-aware stitching.

              `drop_end` drops tokens from the end of input exceeding the model's maximum
              input length.

              `null`, which is the default setting, raises an error if the input exceeds the
              model's maximum input length.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/enrichments",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "texts": texts,
                    "overflow_strategy": overflow_strategy,
                },
                enrichment_create_params.EnrichmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrichmentResponse,
        )


class EnrichmentsResourceWithRawResponse:
    def __init__(self, enrichments: EnrichmentsResource) -> None:
        self._enrichments = enrichments

        self.create = to_raw_response_wrapper(
            enrichments.create,
        )


class AsyncEnrichmentsResourceWithRawResponse:
    def __init__(self, enrichments: AsyncEnrichmentsResource) -> None:
        self._enrichments = enrichments

        self.create = async_to_raw_response_wrapper(
            enrichments.create,
        )


class EnrichmentsResourceWithStreamingResponse:
    def __init__(self, enrichments: EnrichmentsResource) -> None:
        self._enrichments = enrichments

        self.create = to_streamed_response_wrapper(
            enrichments.create,
        )


class AsyncEnrichmentsResourceWithStreamingResponse:
    def __init__(self, enrichments: AsyncEnrichmentsResource) -> None:
        self._enrichments = enrichments

        self.create = async_to_streamed_response_wrapper(
            enrichments.create,
        )
