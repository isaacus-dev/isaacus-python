# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["EmbeddingResponse", "Embedding", "Usage"]


class Embedding(BaseModel):
    index: int
    """
    The position of the content in the input array of contents, starting from `0`
    (and, therefore, ending at the number of contents minus `1`).
    """

    embedding: List[float]
    """The embedding of the content represented as an array of floating point numbers."""


class Usage(BaseModel):
    """Statistics about the usage of resources in the process of embedding the inputs."""

    input_tokens: int
    """The number of tokens inputted to the model."""


class EmbeddingResponse(BaseModel):
    embeddings: List[Embedding]
    """The embeddings of the inputs."""

    usage: Usage
    """Statistics about the usage of resources in the process of embedding the inputs."""
