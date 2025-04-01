# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["Reranking", "Result", "Usage"]


class Result(BaseModel):
    index: int
    """
    The index of the text in the input array of texts, starting from `0` (and,
    therefore, ending at the number of texts minus `1`).
    """

    score: float
    """
    A score between `0` and `1`, inclusive, representing the relevance of the text
    to the query.
    """


class Usage(BaseModel):
    input_tokens: int
    """The number of tokens inputted to the model."""


class Reranking(BaseModel):
    results: List[Result]
    """
    The rerankings of the texts, by relevance to the query, in order from highest to
    lowest relevance score.
    """

    usage: Usage
    """Statistics about the usage of resources in the process of reranking the texts."""
