# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QaCreateParams", "ChunkingOptions"]


class QaCreateParams(TypedDict, total=False):
    model: Required[Literal["kanon-answer-extractor", "kanon-answer-extractor-mini"]]
    """
    The ID of the [model](https://docs.isaacus.com/models#extractive-qa) to use for
    extractive question answering.
    """

    query: Required[str]
    """The query to extract the answer to.

    The query must contain at least one non-whitespace character.

    Unlike the texts from which the answer will be extracted, the query cannot be so
    long that it exceeds the maximum input length of the model.
    """

    texts: Required[List[str]]
    """The texts to search for the answer in and extract the answer from.

    There must be at least one text.

    Each text must contain at least one non-whitespace character.
    """

    chunking_options: Optional[ChunkingOptions]
    """Options for how to split text into smaller chunks."""

    ignore_inextractability: bool
    """
    Whether to, if the model's score of the likelihood that an answer can not be
    extracted from a text is greater than the highest score of all possible answers,
    still return the highest scoring answers for that text.

    If you have already determined that the texts answer the query, for example, by
    using one of our classification or reranker models, then you should set this to
    `true`.
    """

    top_k: int
    """The number of highest scoring answers to return.

    If `null`, which is the default, all answers will be returned.
    """


class ChunkingOptions(TypedDict, total=False):
    overlap_ratio: Optional[float]
    """A number greater than or equal to 0 and less than 1."""

    overlap_tokens: Optional[int]
    """A whole number greater than -1."""

    size: Optional[int]
    """A whole number greater than or equal to 1."""
