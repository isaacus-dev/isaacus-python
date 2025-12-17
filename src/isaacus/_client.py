# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import IsaacusError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import embeddings, rerankings, extractions, classifications
    from .resources.embeddings import EmbeddingsResource, AsyncEmbeddingsResource
    from .resources.rerankings import RerankingsResource, AsyncRerankingsResource
    from .resources.extractions.extractions import ExtractionsResource, AsyncExtractionsResource
    from .resources.classifications.classifications import ClassificationsResource, AsyncClassificationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Isaacus", "AsyncIsaacus", "Client", "AsyncClient"]


class Isaacus(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Isaacus client instance.

        This automatically infers the `api_key` argument from the `ISAACUS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ISAACUS_API_KEY")
        if api_key is None:
            raise IsaacusError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ISAACUS_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ISAACUS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.isaacus.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        from .resources.embeddings import EmbeddingsResource

        return EmbeddingsResource(self)

    @cached_property
    def classifications(self) -> ClassificationsResource:
        from .resources.classifications import ClassificationsResource

        return ClassificationsResource(self)

    @cached_property
    def rerankings(self) -> RerankingsResource:
        from .resources.rerankings import RerankingsResource

        return RerankingsResource(self)

    @cached_property
    def extractions(self) -> ExtractionsResource:
        from .resources.extractions import ExtractionsResource

        return ExtractionsResource(self)

    @cached_property
    def with_raw_response(self) -> IsaacusWithRawResponse:
        return IsaacusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IsaacusWithStreamedResponse:
        return IsaacusWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncIsaacus(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncIsaacus client instance.

        This automatically infers the `api_key` argument from the `ISAACUS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ISAACUS_API_KEY")
        if api_key is None:
            raise IsaacusError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ISAACUS_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ISAACUS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.isaacus.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        from .resources.embeddings import AsyncEmbeddingsResource

        return AsyncEmbeddingsResource(self)

    @cached_property
    def classifications(self) -> AsyncClassificationsResource:
        from .resources.classifications import AsyncClassificationsResource

        return AsyncClassificationsResource(self)

    @cached_property
    def rerankings(self) -> AsyncRerankingsResource:
        from .resources.rerankings import AsyncRerankingsResource

        return AsyncRerankingsResource(self)

    @cached_property
    def extractions(self) -> AsyncExtractionsResource:
        from .resources.extractions import AsyncExtractionsResource

        return AsyncExtractionsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncIsaacusWithRawResponse:
        return AsyncIsaacusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIsaacusWithStreamedResponse:
        return AsyncIsaacusWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class IsaacusWithRawResponse:
    _client: Isaacus

    def __init__(self, client: Isaacus) -> None:
        self._client = client

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithRawResponse:
        from .resources.embeddings import EmbeddingsResourceWithRawResponse

        return EmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def classifications(self) -> classifications.ClassificationsResourceWithRawResponse:
        from .resources.classifications import ClassificationsResourceWithRawResponse

        return ClassificationsResourceWithRawResponse(self._client.classifications)

    @cached_property
    def rerankings(self) -> rerankings.RerankingsResourceWithRawResponse:
        from .resources.rerankings import RerankingsResourceWithRawResponse

        return RerankingsResourceWithRawResponse(self._client.rerankings)

    @cached_property
    def extractions(self) -> extractions.ExtractionsResourceWithRawResponse:
        from .resources.extractions import ExtractionsResourceWithRawResponse

        return ExtractionsResourceWithRawResponse(self._client.extractions)


class AsyncIsaacusWithRawResponse:
    _client: AsyncIsaacus

    def __init__(self, client: AsyncIsaacus) -> None:
        self._client = client

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithRawResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithRawResponse

        return AsyncEmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def classifications(self) -> classifications.AsyncClassificationsResourceWithRawResponse:
        from .resources.classifications import AsyncClassificationsResourceWithRawResponse

        return AsyncClassificationsResourceWithRawResponse(self._client.classifications)

    @cached_property
    def rerankings(self) -> rerankings.AsyncRerankingsResourceWithRawResponse:
        from .resources.rerankings import AsyncRerankingsResourceWithRawResponse

        return AsyncRerankingsResourceWithRawResponse(self._client.rerankings)

    @cached_property
    def extractions(self) -> extractions.AsyncExtractionsResourceWithRawResponse:
        from .resources.extractions import AsyncExtractionsResourceWithRawResponse

        return AsyncExtractionsResourceWithRawResponse(self._client.extractions)


class IsaacusWithStreamedResponse:
    _client: Isaacus

    def __init__(self, client: Isaacus) -> None:
        self._client = client

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import EmbeddingsResourceWithStreamingResponse

        return EmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def classifications(self) -> classifications.ClassificationsResourceWithStreamingResponse:
        from .resources.classifications import ClassificationsResourceWithStreamingResponse

        return ClassificationsResourceWithStreamingResponse(self._client.classifications)

    @cached_property
    def rerankings(self) -> rerankings.RerankingsResourceWithStreamingResponse:
        from .resources.rerankings import RerankingsResourceWithStreamingResponse

        return RerankingsResourceWithStreamingResponse(self._client.rerankings)

    @cached_property
    def extractions(self) -> extractions.ExtractionsResourceWithStreamingResponse:
        from .resources.extractions import ExtractionsResourceWithStreamingResponse

        return ExtractionsResourceWithStreamingResponse(self._client.extractions)


class AsyncIsaacusWithStreamedResponse:
    _client: AsyncIsaacus

    def __init__(self, client: AsyncIsaacus) -> None:
        self._client = client

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithStreamingResponse

        return AsyncEmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def classifications(self) -> classifications.AsyncClassificationsResourceWithStreamingResponse:
        from .resources.classifications import AsyncClassificationsResourceWithStreamingResponse

        return AsyncClassificationsResourceWithStreamingResponse(self._client.classifications)

    @cached_property
    def rerankings(self) -> rerankings.AsyncRerankingsResourceWithStreamingResponse:
        from .resources.rerankings import AsyncRerankingsResourceWithStreamingResponse

        return AsyncRerankingsResourceWithStreamingResponse(self._client.rerankings)

    @cached_property
    def extractions(self) -> extractions.AsyncExtractionsResourceWithStreamingResponse:
        from .resources.extractions import AsyncExtractionsResourceWithStreamingResponse

        return AsyncExtractionsResourceWithStreamingResponse(self._client.extractions)


Client = Isaacus

AsyncClient = AsyncIsaacus
