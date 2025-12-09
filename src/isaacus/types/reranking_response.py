# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RerankingResponse", "Result", "Usage"]


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
    """Statistics about the usage of resources in the process of reranking the texts."""

    input_tokens: int
    """The number of tokens inputted to the model."""


class RerankingResponse(BaseModel):
    """
    The reranking of texts, by relevance to a query, out of an input array of texts.
    """

    results: List[Result]
    """
    The rerankings of the texts, by relevance to the query, in order from highest to
    lowest relevance score.
    """

    usage: Usage
    """Statistics about the usage of resources in the process of reranking the texts."""
