# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["Embedding", "Usage"]


class Usage(BaseModel):
    input_tokens: int
    """The number of tokens inputted to the model."""


class Embedding(BaseModel):
    embeddings: List[Embedding]
    """The embeddings of the inputs."""

    usage: Usage
    """Statistics about the usage of resources in the process of embedding the inputs."""
