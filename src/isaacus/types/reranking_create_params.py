# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RerankingCreateParams", "ChunkingOptions"]


class RerankingCreateParams(TypedDict, total=False):
    model: Required[Literal["kanon-universal-classifier", "kanon-universal-classifier-mini"]]
    """
    The ID of the [model](https://docs.isaacus.com/models#reranking) to use for
    reranking.
    """

    query: Required[str]
    """The query to evaluate the relevance of the texts to.

    The query must contain at least one non-whitespace character.

    Unlike the texts being reranked, the query cannot be so long that it exceeds the
    maximum input length of the reranker.
    """

    texts: Required[List[str]]
    """The texts to rerank.

    There must be at least one text.

    Each text must contain at least one non-whitespace character.
    """

    chunking_options: Optional[ChunkingOptions]
    """Options for how to split text into smaller chunks."""

    is_iql: bool
    """
    Whether the query should be interpreted as an
    [Isaacus Query Language (IQL)](https://docs.isaacus.com/iql) query, which is not
    the case by default.

    If you allow untrusted users to construct their own queries, think carefully
    before enabling IQL since queries can be crafted to consume an excessively large
    amount of tokens.
    """

    scoring_method: Literal["auto", "chunk_max", "chunk_avg", "chunk_min"]
    """The method to use for producing an overall relevance score for a text.

    `auto` is the default scoring method and is recommended for most use cases.
    Currently, it is equivalent to `chunk_max`. In the future, it will automatically
    select the best method based on the model and inputs.

    `chunk_max` uses the highest relevance score of all of a text's chunks.

    `chunk_avg` averages the relevance scores of all of a text's chunks.

    `chunk_min` uses the lowest relevance score of all of a text's chunks.
    """

    top_n: Optional[int]
    """A whole number greater than or equal to 1."""


class ChunkingOptions(TypedDict, total=False):
    overlap_ratio: Optional[float]
    """A number greater than or equal to 0 and less than 1."""

    overlap_tokens: Optional[int]
    """A whole number greater than -1."""

    size: Optional[int]
    """A whole number greater than or equal to 1."""
