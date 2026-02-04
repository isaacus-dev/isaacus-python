# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .ilgs.v1.document import Document

__all__ = ["EnrichmentResponse", "Result", "Usage"]


class Result(BaseModel):
    """An enriched document alongside its index in the input array of texts."""

    index: int
    """
    The index of this document in the input array of texts, starting at `0` (and,
    therefore, ending at the number of inputs minus `1`).
    """

    document: Document
    """The enriched document."""


class Usage(BaseModel):
    """Statistics about the usage of resources in the process of enriching the input."""

    input_tokens: int
    """The total number of tokens inputted to the model."""


class EnrichmentResponse(BaseModel):
    results: List[Result]
    """
    The input documents enriched into version 1.0.0 of the Isaacus Legal Graph
    Schema (IGLS).

    All spans in an enriched document graph are indexed into the Unicode code point
    space of a source document. Access to source documents is thus required to
    resolve spans into text.

    The start and end indices of spans are zero-based (i.e., the first Unicode code
    point in the document is at index 0) and half-open (i.e., the end index is
    exclusive).

    All spans are globally laminar and well-nested similar to XML—it is impossible
    for any two spans to partially overlap; they can only be disjoint, adjacent, or
    wholly nested.

    Spans of the exact same type (e.g., segments) will never be duplicated.

    Spans cannot be empty and will never start or end at whitespace.

    When using programming languages other than Python (which uses zero-based,
    half-open, Unicode code point-spaced string indexing), indices may need to be
    translated accordingly (for example, JavaScript slices into UTF-16 code units
    instead of Unicode code points).
    """

    usage: Usage
    """Statistics about the usage of resources in the process of enriching the input."""
