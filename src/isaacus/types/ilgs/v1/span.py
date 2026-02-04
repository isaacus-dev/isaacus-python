# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["Span"]


class Span(BaseModel):
    """A zero-based, half-open span into the Unicode code point space of input text.

    All spans are globally laminar and well-nested similar to XML—it is impossible for any two spans to partially overlap; they can only be disjoint, adjacent, or wholly nested. Spans of the exact same type (e.g., segments) will never be duplicated.

    A span cannot be empty and will never start or end at whitespace.

    Note that, when using programming languages other than Python (which uses zero-based, half-open, Unicode code point-spaced string indexing), indices may need to be translated accordingly (for example, JavaScript slices into UTF-16 code units instead of Unicode code points).
    """

    start: int
    """
    The zero-based start index of the half-open span of Unicode code points in the
    input text.
    """

    end: int
    """
    The zero-based end index of the half-open span (i.e., the end is exclusive) of
    Unicode code points in the input text.
    """
