# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .span import Span
from ...._models import BaseModel

__all__ = ["Segment"]


class Segment(BaseModel):
    """
    A segment within the document representing a structurally distinct portion of the document's content.
    """

    id: str
    """
    The unique identifier of the segment in the format `seg:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
    """

    kind: Literal["container", "unit", "item", "figure"]
    """
    The structural 'kind' of the segment, being one of `container`, `unit`, `item`,
    or `figure`.

    A `container` is a structural or semantic grouping of content such as a chapter.
    It can contain segments of any kind or none at all.

    A `unit` is a single syntactically independent unit of text such as a paragraph.
    It can only contain `item`s and `figure`s.

    An `item` is a syntactically subordinate unit of text such as an item in a
    run-in list. It can only contain other `item`s. Note that an `item` is
    conceptually distinct from a list item—it is perfectly possible to encounter
    list items that are syntactically independent of their surrounding items just as
    it is possible to encounter dependent clauses that do not appear as part of a
    list.

    A `figure` is a visually structured or tabular unit of content such as a
    diagram, equation, or table. It cannot contain segments.
    """

    type: Optional[
        Literal[
            "title",
            "book",
            "part",
            "chapter",
            "subchapter",
            "division",
            "subdivision",
            "subpart",
            "subtitle",
            "table_of_contents",
            "article",
            "section",
            "regulation",
            "rule",
            "clause",
            "paragraph",
            "subarticle",
            "subsection",
            "subregulation",
            "subrule",
            "subclause",
            "subparagraph",
            "item",
            "subitem",
            "point",
            "indent",
            "schedule",
            "annex",
            "appendix",
            "exhibit",
            "recital",
            "signature",
            "note",
            "figure",
            "table",
            "formula",
        ]
    ] = None
    """
    The addressable 'type' of the segment within the document's referential scheme
    and hierarchy, whether defined explicitly (e.g., by headings, such as
    'Section 2. Definitions'), implicitly (e.g., by way of reference, such as 'as
    defined in Section 2'), or by convention (e.g., [42] in a judgment often denotes
    a `paragraph`, independent provisions in statute are often `section`s, etc.). If
    the type is not known or not applicable, it will be set to `null`.

    Note that, although many segment types may coincide with syntactic constructs,
    they should be thought of purely as distinct formal citable units. Most
    paragraphs (in the syntactic sense) will not have the `paragraph` type, for
    example. That type is reserved for segments that would formally be cited as a
    'Paragraph' within the document's referential scheme.

    The following types are currently supported: `title`, `book`, `part`, `chapter`,
    `subchapter`, `division`, `subdivision`, `subpart`, `subtitle`,
    `table_of_contents`, `article`, `section`, `regulation`, `rule`, `clause`,
    `paragraph`, `subarticle`, `subsection`, `subregulation`, `subrule`,
    `subclause`, `subparagraph`, `item`, `subitem`, `point`, `indent`, `schedule`,
    `annex`, `appendix`, `exhibit`, `recital`, `signature`, `note`, `figure`,
    `table`, and `formula`.

    The `title`, `book`, `part`, `chapter`, `subchapter`, `division`, `subdivision`,
    `subpart`, `subtitle`, and `table_of_contents` types are exclusive to the
    `container` kind.

    The `figure` kind only supports the `figure`, `table`, and `formula` types, all
    of which are exclusive to it.
    """

    category: Literal["front_matter", "scope", "main", "annotation", "back_matter", "other"]
    """
    The functional 'category' of the segment within the document, being one of
    `front_matter`, `scope`, `main`, `annotation`, `back_matter`, or `other`.

    `front_matter` denotes non-operative contextualizing content occurring at the
    start of a document such as a preamble or recitals.

    `scope` denotes operative content defining the application or interpretation of
    a document such as definition sections and governing law clauses.

    `main` denotes operative, non-scopal content.

    `annotation` denotes non-operative annotative content providing explanatory or
    referential information such as commentary, footnotes, and endnotes.

    `back_matter` denotes non-operative contextualizing content occurring at the end
    of a document such as authority statements.

    `other` denotes content that does not fit into any of the other categories.
    """

    type_name: Optional[Span] = None
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

    code: Optional[Span] = None
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

    title: Optional[Span] = None
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

    parent: Optional[str] = None
    """
    A unique identifier for a segment in the format `seg:{index}` where `{index}` is
    a non-negative incrementing integer starting from zero.
    """

    span: Span
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
