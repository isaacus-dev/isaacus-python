# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .date import Date
from .span import Span
from .term import Term
from .email import Email
from .quote import Quote
from .person import Person
from .segment import Segment
from .website import Website
from .location import Location
from .id_number import IDNumber
from ...._models import BaseModel
from .phone_number import PhoneNumber
from .crossreference import Crossreference
from .external_document import ExternalDocument

__all__ = ["Document"]


class Document(BaseModel):
    """
    The document enriched into version 1.0.0 of the [Isaacus Legal Graph Schema (ILGS)](https://docs.isaacus.com/ilgs).

    All spans in an enriched document graph are indexed into the Unicode code point space of a source document.

    The start and end indices of spans are zero-based (i.e., the first Unicode code point in the document is at index 0) and half-open (i.e., the end index is exclusive).

    All spans are globally laminar and well-nested similar to XML—it is impossible for any two spans to partially overlap; they can only be disjoint, adjacent, or wholly nested.

    Spans of the exact same type (e.g., segments) will never be duplicated.

    Spans cannot be empty and will never start or end at whitespace.

    When using programming languages other than Python (which uses zero-based, half-open, Unicode code point-spaced string indexing), indices may need to be translated accordingly (for example, JavaScript slices into UTF-16 code units instead of Unicode code points).
    """

    text: str
    """The text of the document."""

    title: Optional[Span] = None
    """A zero-based, half-open span into the Unicode code point space of input text.

    All spans are globally laminar and well-nested similar to XML—it is impossible
    for any two spans to partially overlap; they can only be disjoint, adjacent, or
    wholly nested. Spans of the exact same type (e.g., segments) will never be
    duplicated.

    A span cannot be empty and will never start or end at whitespace (though a
    span's `end` index, being an exclusive index, may obviosuly land on a whitespace
    character).

    Note that, when using programming languages other than Python (which uses
    zero-based, half-open, Unicode code point-spaced string indexing), indices may
    need to be translated accordingly (for example, JavaScript slices into UTF-16
    code units instead of Unicode code points).
    """

    subtitle: Optional[Span] = None
    """A zero-based, half-open span into the Unicode code point space of input text.

    All spans are globally laminar and well-nested similar to XML—it is impossible
    for any two spans to partially overlap; they can only be disjoint, adjacent, or
    wholly nested. Spans of the exact same type (e.g., segments) will never be
    duplicated.

    A span cannot be empty and will never start or end at whitespace (though a
    span's `end` index, being an exclusive index, may obviosuly land on a whitespace
    character).

    Note that, when using programming languages other than Python (which uses
    zero-based, half-open, Unicode code point-spaced string indexing), indices may
    need to be translated accordingly (for example, JavaScript slices into UTF-16
    code units instead of Unicode code points).
    """

    type: Literal["statute", "regulation", "decision", "contract", "other"]
    """
    The type of the document, being one of `statute`, `regulation`, `decision`,
    `contract`, or `other`.

    `statute` denotes primary legislation such as acts, bills, codes, and
    constitutions.

    `regulation` denotes secondary legislation such as rules, statutory instruments,
    and ordinances.

    `decision` denotes judicial or quasi-judicial decisions such as court judgments,
    judicial opinions, and tribunal rulings.

    `contract` denotes contracts, covenants, and agreements.

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

    segments: List[Segment]
    """
    An array of segments within the document representing structurally distinct
    portions of its content.
    """

    crossreferences: List[Crossreference]
    """
    An array of cross-references within the document pointing to a single segment or
    a span of segments.
    """

    locations: List[Location]
    """An array of locations identified in the document."""

    persons: List[Person]
    """An array of legal persons identified in the document."""

    emails: List[Email]
    """
    An array of email addresses identified in the document belonging to legal
    persons.

    Email addresses mentioned in the document that are not attributable to legal
    persons will not be extracted.
    """

    websites: List[Website]
    """An array of websites identified in the document belonging to legal persons.

    Websites mentioned in the document that are not attributable to legal persons
    will not be extracted.
    """

    phone_numbers: List[PhoneNumber]
    """
    An array of valid phone numbers identified in the document belonging to legal
    persons.

    Phone numbers mentioned in the document that are not valid, possible, or
    attributable to legal persons will not be extracted.
    """

    id_numbers: List[IDNumber]
    """
    An array of identification numbers identified in the document belonging to legal
    persons.

    Identification numbers mentioned in the document that are not attributable to
    legal persons will not be extracted.
    """

    terms: List[Term]
    """An array of terms assigned definite meanings within the document."""

    external_documents: List[ExternalDocument]
    """An array of documents identified within the document."""

    quotes: List[Quote]
    """An array of quotations within the document."""

    dates: List[Date]
    """
    An array of dates identified in the document belonging to one of the following
    types: `creation`, `signature`, `effective`, `expiry`, `delivery`, `renewal`,
    `payment`, `birth`, or `death`.

    Only full Gregorian dates (i.e., including a day, month, and year) between the
    years 1000 and 9999 (inclusive) fitting into one of the supported date types are
    extractable.
    """

    headings: List[Span]
    """An array of spans within the document's text constituting headings."""

    junk: List[Span]
    """
    An array of spans within the document's text constituting non-operative,
    non-substantive 'junk' content such as headers, footers, page numbers, and OCR
    artifacts.
    """

    version: Literal["ilgs@1"]
