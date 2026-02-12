# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .span import Span
from ...._models import BaseModel

__all__ = ["ExternalDocument"]


class ExternalDocument(BaseModel):
    """A document identified within another document."""

    id: str
    """
    The unique identifier of the external document in the format `exd:{identifier}`.
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

    type: Literal["statute", "regulation", "decision", "contract", "other"]
    """
    The type of the external document, being one of `statute`, `regulation`,
    `decision`, `contract`, or `other`.

    `statute` denotes primary legislation such as acts, bills, codes, and
    constitutions.

    `regulation` denotes secondary legislation such as rules, statutory instruments,
    and ordinances.

    `decision` denotes judicial or quasi-judicial decisions such as court judgments,
    judicial opinions, and tribunal rulings.

    `other` is used for all other types of legal documents that do not fit into any
    of the predefined types.
    """

    jurisdiction: Optional[str] = None
    """
    A jurisdiction code representing a country (via an initial country code) and,
    optionally, a subdivision within that country (via a subsequent subdivision code
    prefixed by a hyphen).

    All 249 ISO 3166-1 alpha-2 country codes are representable in addition to
    special `INT` and `EU` codes for international and European Union law,
    respectively.

    All 5,046 ISO 3166-2 codes are also representable in addition to a special `FED`
    code for federal law.
    """

    reception: Literal["positive", "mixed", "negative", "neutral"]
    """
    The sentiment of the document towards the external document, being one of
    `positive`, `mixed`, `negative`, or `neutral`.

    `positive` indicates that the document expresses a favorable view of the
    external document whether by endorsing or approving it.

    `mixed` indicates that the document expresses both favorable and unfavorable
    views of the external document, for example, by affirming parts of it and
    disapproving others.

    `negative` indicates that the document expresses an unfavorable view of the
    external document whether by criticizing, repealing, overruling, or explicitly
    contradicting it.

    `neutral` indicates that the document references the external document without
    expressing any particular sentiment towards it.
    """

    mentions: List[Span]
    """
    An array of one or more spans within the document's text where the external
    document is mentioned by name, for example, 'the US Constitution' in 'the Second
    Amendment to the US Constitution protects freedom of speech'.
    """

    pinpoints: List[Span]
    """
    An array of spans within the document's text where specific parts of the
    external document are referenced, for example, 'Section 2' in 'as defined in
    Section 2 of the US Constitution'.
    """
