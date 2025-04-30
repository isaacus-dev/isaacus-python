# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.extractions import qa_create_params
from ...types.extractions.answer_extraction import AnswerExtraction

__all__ = ["QaResource", "AsyncQaResource"]


class QaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return QaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return QaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["kanon-answer-extractor", "kanon-answer-extractor-mini"],
        query: str,
        texts: List[str],
        chunking_options: Optional[qa_create_params.ChunkingOptions] | NotGiven = NOT_GIVEN,
        ignore_inextractability: bool | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnswerExtraction:
        """
        Extract answers to questions from legal documents with an Isaacus legal AI
        answer extractor.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#extractive-qa) to use for
              extractive question answering.

          query: The query to extract the answer to.

              The query must contain at least one non-whitespace character.

              Unlike the texts from which the answer will be extracted, the query cannot be so
              long that it exceeds the maximum input length of the model.

          texts: The texts to search for the answer in and extract the answer from.

              There must be at least one text.

              Each text must contain at least one non-whitespace character.

          chunking_options: Options for how to split text into smaller chunks.

          ignore_inextractability: Whether to, if the model's score of the likelihood that an answer can not be
              extracted from a text is greater than the highest score of all possible answers,
              still return the highest scoring answers for that text.

              If you have already determined that the texts answer the query, for example, by
              using one of our classification or reranker models, then you should set this to
              `true`.

          top_k: The number of highest scoring answers to return.

              If `null`, which is the default, all answers will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extractions/qa",
            body=maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "texts": texts,
                    "chunking_options": chunking_options,
                    "ignore_inextractability": ignore_inextractability,
                    "top_k": top_k,
                },
                qa_create_params.QaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerExtraction,
        )


class AsyncQaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/isaacus-dev/isaacus-python#with_streaming_response
        """
        return AsyncQaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["kanon-answer-extractor", "kanon-answer-extractor-mini"],
        query: str,
        texts: List[str],
        chunking_options: Optional[qa_create_params.ChunkingOptions] | NotGiven = NOT_GIVEN,
        ignore_inextractability: bool | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnswerExtraction:
        """
        Extract answers to questions from legal documents with an Isaacus legal AI
        answer extractor.

        Args:
          model: The ID of the [model](https://docs.isaacus.com/models#extractive-qa) to use for
              extractive question answering.

          query: The query to extract the answer to.

              The query must contain at least one non-whitespace character.

              Unlike the texts from which the answer will be extracted, the query cannot be so
              long that it exceeds the maximum input length of the model.

          texts: The texts to search for the answer in and extract the answer from.

              There must be at least one text.

              Each text must contain at least one non-whitespace character.

          chunking_options: Options for how to split text into smaller chunks.

          ignore_inextractability: Whether to, if the model's score of the likelihood that an answer can not be
              extracted from a text is greater than the highest score of all possible answers,
              still return the highest scoring answers for that text.

              If you have already determined that the texts answer the query, for example, by
              using one of our classification or reranker models, then you should set this to
              `true`.

          top_k: The number of highest scoring answers to return.

              If `null`, which is the default, all answers will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extractions/qa",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "texts": texts,
                    "chunking_options": chunking_options,
                    "ignore_inextractability": ignore_inextractability,
                    "top_k": top_k,
                },
                qa_create_params.QaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerExtraction,
        )


class QaResourceWithRawResponse:
    def __init__(self, qa: QaResource) -> None:
        self._qa = qa

        self.create = to_raw_response_wrapper(
            qa.create,
        )


class AsyncQaResourceWithRawResponse:
    def __init__(self, qa: AsyncQaResource) -> None:
        self._qa = qa

        self.create = async_to_raw_response_wrapper(
            qa.create,
        )


class QaResourceWithStreamingResponse:
    def __init__(self, qa: QaResource) -> None:
        self._qa = qa

        self.create = to_streamed_response_wrapper(
            qa.create,
        )


class AsyncQaResourceWithStreamingResponse:
    def __init__(self, qa: AsyncQaResource) -> None:
        self._qa = qa

        self.create = async_to_streamed_response_wrapper(
            qa.create,
        )
