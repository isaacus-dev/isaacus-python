# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .qa.qa import (
    QAResource,
    AsyncQAResource,
    QAResourceWithRawResponse,
    AsyncQAResourceWithRawResponse,
    QAResourceWithStreamingResponse,
    AsyncQAResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExtractionsResource", "AsyncExtractionsResource"]


class ExtractionsResource(SyncAPIResource):
    @cached_property
    def qa(self) -> QAResource:
        return QAResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return ExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return ExtractionsResourceWithStreamingResponse(self)


class AsyncExtractionsResource(AsyncAPIResource):
    @cached_property
    def qa(self) -> AsyncQAResource:
        return AsyncQAResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return AsyncExtractionsResourceWithStreamingResponse(self)


class ExtractionsResourceWithRawResponse:
    def __init__(self, extractions: ExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def qa(self) -> QAResourceWithRawResponse:
        return QAResourceWithRawResponse(self._extractions.qa)


class AsyncExtractionsResourceWithRawResponse:
    def __init__(self, extractions: AsyncExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def qa(self) -> AsyncQAResourceWithRawResponse:
        return AsyncQAResourceWithRawResponse(self._extractions.qa)


class ExtractionsResourceWithStreamingResponse:
    def __init__(self, extractions: ExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def qa(self) -> QAResourceWithStreamingResponse:
        return QAResourceWithStreamingResponse(self._extractions.qa)


class AsyncExtractionsResourceWithStreamingResponse:
    def __init__(self, extractions: AsyncExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def qa(self) -> AsyncQAResourceWithStreamingResponse:
        return AsyncQAResourceWithStreamingResponse(self._extractions.qa)
