# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .span import Span
from .._models import BaseModel

__all__ = ["Term"]


class Term(BaseModel):
    """A term assigned a definite meaning within a document."""

    id: str
    """
    The unique identifier of the term in the format `term:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
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

    meaning: Span
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

    mentions: List[Span]
    """
    An array of spans within the document's text where the term is mentioned outside
    of its definition.

    It is possible for the term to have no mentions if, outside of its definition,
    it is never referred to in the document.
    """
