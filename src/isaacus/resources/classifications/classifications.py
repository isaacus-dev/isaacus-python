# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .universal import (
    UniversalResource,
    AsyncUniversalResource,
    UniversalResourceWithRawResponse,
    AsyncUniversalResourceWithRawResponse,
    UniversalResourceWithStreamingResponse,
    AsyncUniversalResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ClassificationsResource", "AsyncClassificationsResource"]


class ClassificationsResource(SyncAPIResource):
    @cached_property
    def universal(self) -> UniversalResource:
        return UniversalResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClassificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return ClassificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return ClassificationsResourceWithStreamingResponse(self)


class AsyncClassificationsResource(AsyncAPIResource):
    @cached_property
    def universal(self) -> AsyncUniversalResource:
        return AsyncUniversalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClassificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return AsyncClassificationsResourceWithStreamingResponse(self)


class ClassificationsResourceWithRawResponse:
    def __init__(self, classifications: ClassificationsResource) -> None:
        self._classifications = classifications

    @cached_property
    def universal(self) -> UniversalResourceWithRawResponse:
        return UniversalResourceWithRawResponse(self._classifications.universal)


class AsyncClassificationsResourceWithRawResponse:
    def __init__(self, classifications: AsyncClassificationsResource) -> None:
        self._classifications = classifications

    @cached_property
    def universal(self) -> AsyncUniversalResourceWithRawResponse:
        return AsyncUniversalResourceWithRawResponse(self._classifications.universal)


class ClassificationsResourceWithStreamingResponse:
    def __init__(self, classifications: ClassificationsResource) -> None:
        self._classifications = classifications

    @cached_property
    def universal(self) -> UniversalResourceWithStreamingResponse:
        return UniversalResourceWithStreamingResponse(self._classifications.universal)


class AsyncClassificationsResourceWithStreamingResponse:
    def __init__(self, classifications: AsyncClassificationsResource) -> None:
        self._classifications = classifications

    @cached_property
    def universal(self) -> AsyncUniversalResourceWithStreamingResponse:
        return AsyncUniversalResourceWithStreamingResponse(self._classifications.universal)
