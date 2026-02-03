# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .ilgs_v1_span import IlgsV1Span

__all__ = ["IlgsV1Quote"]


class IlgsV1Quote(BaseModel):
    """A quotation within a document."""

    amending: bool
    """
    Whether the quote is being used to amend or modify content, typically in other
    documents.
    """

    source_document: Optional[str] = None
    """
    A unique identifier for an external document in the format `exd:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    source_person: Optional[str] = None
    """
    A unique identifier for a legal person in the format `per:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    source_segment: Optional[str] = None
    """
    A unique identifier for a segment in the format `seg:{index}` where `{index}` is
    a non-negative incrementing integer starting from zero.
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
