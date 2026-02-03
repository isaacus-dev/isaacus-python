# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ilgs_v1_date import IlgsV1Date
from .ilgs_v1_span import IlgsV1Span
from .ilgs_v1_term import IlgsV1Term
from .ilgs_v1_email import IlgsV1Email
from .ilgs_v1_quote import IlgsV1Quote
from .ilgs_v1_person import IlgsV1Person
from .ilgs_v1_segment import IlgsV1Segment
from .ilgs_v1_website import IlgsV1Website
from .ilgs_v1_location import IlgsV1Location
from .ilgs_v1_id_number import IlgsV1IDNumber
from .ilgs_v1_phone_number import IlgsV1PhoneNumber
from .ilgs_v1_crossreference import IlgsV1Crossreference
from .ilgs_v1_external_document import IlgsV1ExternalDocument

__all__ = ["IlgsV1Document"]


class IlgsV1Document(BaseModel):
    """The enriched document."""

    crossreferences: List[IlgsV1Crossreference]
    """
    An array of cross-references within the document pointing to a single segment or
    a span of segments.
    """

    dates: List[IlgsV1Date]
    """
    An array of dates identified in the document belonging to one of the following
    types: `creation`, `signature`, `effective`, `expiry`, `delivery`, `renewal`,
    `payment`, `birth`, or `death`.

    Only Gregorian dates between the years 1000 and 9999 (inclusive) fitting into
    one of the supported date types are extractable.
    """

    emails: List[IlgsV1Email]
    """
    An array of email addresses identified in the document belonging to legal
    persons.

    Email addresses mentioned in the document that are not attributable to legal
    persons will not be extracted.
    """

    external_documents: List[IlgsV1ExternalDocument]
    """An array of documents identified within the document."""

    headings: List[IlgsV1Span]
    """An array of spans within the document's text constituting headings."""

    id_numbers: List[IlgsV1IDNumber]
    """
    An array of identification numbers identified in the document belonging to legal
    persons.

    Identification numbers mentioned in the document that are not attributable to
    legal persons will not be extracted.
    """

    junk: List[IlgsV1Span]
    """
    An array of spans within the document's text constituting non-operative,
    non-substantive 'junk' content such as headers, footers, page numbers, and OCR
    artifacts.
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

    locations: List[IlgsV1Location]
    """An array of locations identified in the document."""

    persons: List[IlgsV1Person]
    """An array of legal persons identified in the document."""

    phone_numbers: List[IlgsV1PhoneNumber]
    """
    An array of valid phone numbers identified in the document belonging to legal
    persons.

    Phone numbers mentioned in the document that are not valid, possible, or
    attributable to legal persons will not be extracted.
    """

    quotes: List[IlgsV1Quote]
    """An array of quotations within the document."""

    segments: List[IlgsV1Segment]
    """
    An array of segments within the document representing structurally distinct
    portions of its content.
    """

    subtitle: Optional[IlgsV1Span] = None
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

    terms: List[IlgsV1Term]
    """An array of terms assigned definite meanings within the document."""

    title: Optional[IlgsV1Span] = None
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
    The type of the document, being one of `statute`, `regulation`, `decision`,
    `contract`, or `other`.

    `statute` denotes primary legislation such as acts, bills, codes, and
    constitutions.

    `regulation` denotes secondary legislation such as rules, statutory instruments,
    and ordinances.

    `decision` denotes judicial or quasi-judicial decisions such as court judgments,
    judicial opinions, and tribunal rulings.

    `other` is used for all other types of legal documents that do not fit into any
    of the predefined types.
    """

    version: Literal["ilgs@1"]

    websites: List[IlgsV1Website]
    """An array of websites identified in the document belonging to legal persons.

    Websites mentioned in the document that are not attributable to legal persons
    will not be extracted.
    """
