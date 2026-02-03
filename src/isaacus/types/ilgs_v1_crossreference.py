# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .ilgs_v1_span import IlgsV1Span

__all__ = ["IlgsV1Crossreference"]


class IlgsV1Crossreference(BaseModel):
    """A cross-reference within the document pointing to one or more segments."""

    end: str
    """
    The unique identifier of the latest segment in the span of segments being
    cross-referenced with ties broken in favor of the least-nested (i.e., largest)
    segment. If the cross-reference points to a single segment, `start` and `end`
    will be identical.
    """

    span: IlgsV1Span
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

    start: str
    """
    The unique identifier of the earliest segment in the span of segments being
    cross-referenced with ties broken in favor of the least-nested (i.e., largest)
    segment. If the cross-reference points to a single segment, `start` and `end`
    will be identical.
    """
