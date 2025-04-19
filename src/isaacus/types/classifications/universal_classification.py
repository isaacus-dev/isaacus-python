# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UniversalClassification", "Classification", "ClassificationChunk", "Usage"]


class ClassificationChunk(BaseModel):
    end: int
    """
    The index of the character immediately after the last character of the chunk in
    the original text, beginning from `0` (such that, in Python, the chunk is
    equivalent to `text[start:end]`).
    """

    index: int
    """
    The original position of the chunk in the outputted list of chunks before
    sorting, starting from `0` (and, therefore, ending at the number of chunks minus
    `1`).
    """

    score: float
    """
    The model's score of the likelihood that the query expressed about the chunk is
    supported by the chunk.

    A score greater than `0.5` indicates that the chunk supports the query, while a
    score less than `0.5` indicates that the chunk does not support the query.
    """

    start: int
    """
    The index of the character in the original text where the chunk starts,
    beginning from `0`.
    """

    text: str
    """The text of the chunk."""


class Classification(BaseModel):
    chunks: Optional[List[ClassificationChunk]] = None
    """
    The text as broken into chunks by
    [semchunk](https://github.com/isaacus-dev/semchunk), each chunk with its own
    confidence score, ordered from highest to lowest score.

    If no chunking occurred, this will be `null`.
    """

    index: int
    """
    The index of the text in the input array of texts, starting from `0` (and,
    therefore, ending at the number of texts minus `1`).
    """

    score: float
    """
    A score of the likelihood that the query expressed about the text is supported
    by the text.

    A score greater than `0.5` indicates that the text supports the query, while a
    score less than `0.5` indicates that the text does not support the query.
    """


class Usage(BaseModel):
    input_tokens: int
    """The number of tokens inputted to the model."""


class UniversalClassification(BaseModel):
    classifications: List[Classification]
    """
    The classifications of the texts, by relevance to the query, in order from
    highest to lowest relevance score.
    """

    usage: Usage
    """Statistics about the usage of resources in the process of classifying the text."""
