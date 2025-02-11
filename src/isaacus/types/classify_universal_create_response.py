# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ClassifyUniversalCreateResponse", "Chunk"]


class Chunk(BaseModel):
    confidence: float

    end: int

    start: int

    text: str


class ClassifyUniversalCreateResponse(BaseModel):
    chunks: List[Chunk]
