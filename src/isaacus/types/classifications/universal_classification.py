# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UniversalClassification", "Chunk", "Usage"]


class Chunk(BaseModel):
    end: int
    """The end index of the chunk in the original text."""

    score: float
    """
    The model's score of the likelihood that the query expressed about the chunk is
    supported by the chunk.

    A score greater than `0.5` indicates that the chunk supports the query, while a
    score less than `0.5` indicates that the chunk does not support the query.
    """

    start: int
    """The start index of the chunk in the original text."""

    text: str
    """The text of the chunk."""


class Usage(BaseModel):
    input_tokens: int
    """The number of tokens inputted to the model."""


class UniversalClassification(BaseModel):
    chunks: Optional[List[Chunk]] = None
    """
    The text as broken into chunks by
    [semchunk](https://github.com/isaacus-dev/semchunk), each chunk with its own
    confidence score.

    If no chunking occurred, this will be `null`.
    """

    score: float
    """
    A score of the likelihood that the query expressed about the text is supported
    by the text.

    A score greater than `0.5` indicates that the text supports the query, while a
    score less than `0.5` indicates that the text does not support the query.
    """

    usage: Usage
    """Statistics about the usage of resources in the process of classifying the text."""
