# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UniversalCreateParams", "ChunkingOptions"]


class UniversalCreateParams(TypedDict, total=False):
    model: Required[Literal["kanon-universal-classifier", "kanon-universal-classifier-mini"]]
    """
    The ID of the [model](https://docs.isaacus.com/models#universal-classification)
    to use for universal classification.
    """

    query: Required[str]
    """
    The [Isaacus Query Language (IQL)](https://docs.isaacus.com/iql) query or, if
    IQL is disabled, the statement, to evaluate the texts against.

    The query must contain at least one non-whitespace character.

    Unlike the texts being classified, the query cannot be so long that it exceeds
    the maximum input length of the universal classifier.
    """

    texts: Required[List[str]]
    """The texts to classify.

    Each text must contain at least one non-whitespace character.
    """

    chunking_options: Optional[ChunkingOptions]
    """Options for how to split text into smaller chunks."""

    is_iql: bool
    """
    Whether the query should be interpreted as an
    [IQL](https://docs.isaacus.com/iql) query or else as a statement.
    """

    scoring_method: Literal["auto", "chunk_max", "chunk_avg", "chunk_min"]
    """The method to use for producing an overall confidence score.

    `auto` is the default scoring method and is recommended for most use cases.
    Currently, it is equivalent to `chunk_max`. In the future, it will automatically
    select the best method based on the model and inputs.

    `chunk_max` uses the highest confidence score of all of the texts' chunks.

    `chunk_avg` averages the confidence scores of all of the texts' chunks.

    `chunk_min` uses the lowest confidence score of all of the texts' chunks.
    """


class ChunkingOptions(TypedDict, total=False):
    overlap_ratio: Optional[float]
    """A number greater than or equal to 0 and less than 1."""

    overlap_tokens: Optional[int]
    """A whole number greater than -1."""

    size: Optional[int]
    """A whole number greater than or equal to 1."""
