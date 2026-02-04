# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .span import Span
from ...._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
    """A location identified within a document."""

    id: str
    """
    The unique identifier of the location in the format `loc:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    name: Span
    """A zero-based, half-open span into the Unicode code point space of input text.

    All spans are globally laminar and well-nested similar to XML—it is impossible
    for any two spans to partially overlap; they can only be disjoint, adjacent, or
    wholly nested. Spans of the exact same type (e.g., segments) will never be
    duplicated.

    A span cannot be empty and will never start or end at whitespace.

    Note that, when using programming languages other than Python (which uses
    zero-based, half-open, Unicode code point-spaced string indexing), indices may
    need to be translated accordingly (for example, JavaScript slices into UTF-16
    code units instead of Unicode code points).
    """

    type: Literal["country", "state", "city", "address", "other"]
    """
    The type of the location, being one of `country`, `state`, `city`, `address`, or
    `other`.
    """

    parent: Optional[str] = None
    """
    A unique identifier for a location in the format `loc:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
    """

    mentions: List[Span]
    """
    An array of one or more spans within the document's text where the location is
    mentioned.
    """
