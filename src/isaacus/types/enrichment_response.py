# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "EnrichmentResponse",
    "Result",
    "ResultDocument",
    "ResultDocumentCrossreference",
    "ResultDocumentDate",
    "ResultDocumentEmail",
    "ResultDocumentExternalDocument",
    "ResultDocumentIDNumber",
    "ResultDocumentLocation",
    "ResultDocumentPerson",
    "ResultDocumentPhoneNumber",
    "ResultDocumentQuote",
    "ResultDocumentSegment",
    "ResultDocumentTerm",
    "ResultDocumentWebsite",
    "Usage",
]


class ResultDocumentCrossreference(BaseModel):
    """A cross-reference within the document pointing to one or more segments."""

    end: str
    """
    The unique identifier of the latest segment in the span of segments being
    cross-referenced with ties broken in favor of the least-nested (i.e., largest)
    segment. If the cross-reference points to a single segment, `start` and `end`
    will be identical.
    """

    span: List[object]
    """The span within the document's text where the cross-reference occurs."""

    start: str
    """
    The unique identifier of the earliest segment in the span of segments being
    cross-referenced with ties broken in favor of the least-nested (i.e., largest)
    segment. If the cross-reference points to a single segment, `start` and `end`
    will be identical.
    """


class ResultDocumentDate(BaseModel):
    """
    A date identified in a document belonging to one of the following types: `creation`, `signature`, `effective`, `expiry`, `delivery`, `renewal`, `payment`, `birth`, or `death`.

    Only Gregorian dates between the years 1000 and 9999 (inclusive) fitting into one of the supported date types are extractable.
    """

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the date is
    mentioned.
    """

    person: Optional[str] = None
    """
    A unique identifier for a legal person in the format `per:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    type: Literal["creation", "signature", "effective", "expiry", "delivery", "renewal", "payment", "birth", "death"]
    """
    The type of the date, being one of `creation`, `signature`, `effective`,
    `expiry`, `delivery`, `renewal`, `payment`, `birth`, or `death`. If a date is
    mentioned in a document that does not fit into a supported type, it will not be
    extracted.

    `creation` denotes the date the document was created. There may only be one
    `creation` date per document.

    `signature` denotes the date the document was signed.

    `effective` denotes the date when the document or a part thereof comes into
    effect (e.g., commencement or enactment dates).

    `expiry` denotes the date when the document or a part thereof is no longer in
    effect.

    `delivery` denotes the date when goods or services are to be delivered under the
    document.

    `renewal` denotes the date when one or more of the document's terms are to be
    renewed.

    `payment` denotes the date when payment is to be made under the document.

    `birth` denotes the birth date of a natural person or establishment (e.g.,
    incorporation) date of a non-natural legal person identified in the document.
    There can only be one `birth` date linked to a single person and all `birth`
    dates must be linked to a person. A person's `birth` date will never be after
    their `death` date.

    `death` denotes the death date of a natural person or dissolution date of a
    non-natural legal person identified in the document. There can only be one
    `death` date linked to a single person and all `death` dates must be linked to a
    person. A person's `death` date will never be before their `birth` date.
    """

    value: str
    """The date in ISO 8601 format (YYYY-MM-DD)."""


class ResultDocumentEmail(BaseModel):
    """An email address identified in a document belonging to a legal person.

    If an email address was mentioned in the document but is not attributable to a legal person, it will not be extracted.
    """

    address: str
    """The normalized email address."""

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the email address
    is mentioned.
    """

    person: str
    """The unique identifier of the person that this email address belongs to."""


class ResultDocumentExternalDocument(BaseModel):
    """A document identified within another document."""

    id: str
    """
    The unique identifier of the external document in the format `exd:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
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

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the external
    document is mentioned by name, for example, 'the US Constitution' in 'the Second
    Amendment to the US Constitution protects freedom of speech'.
    """

    name: List[object]
    """
    A span within the document's text representing the 'most proper' name of the
    external document.

    As an example, a document referred to as the 'Constitution of the United States
    of America' in two places in a document, the 'U.S. Constitution' in three
    places, and the 'Constitution' in one place would have its `name` set to
    whichever span the model was most confident represented the proper name of the
    document, likely being one of the 'Constitution of the United States of America'
    spans.
    """

    pinpoints: List[List[object]]
    """
    An array of spans within the document's text where specific parts of the
    external document are referenced, for example, 'Section 2' in 'as defined in
    Section 2 of the US Constitution'.
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


class ResultDocumentIDNumber(BaseModel):
    """An identification number mentioned in a document belonging to a legal person.

    If an identification number was mentioned in the document but is not attributable to a legal person, it will not be extracted.
    """

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the
    identification number is mentioned.
    """

    number: str
    """The identification number."""

    person: str
    """The unique identifier of the person that this identification number belongs to."""


class ResultDocumentLocation(BaseModel):
    """A location identified within a document."""

    id: str
    """
    The unique identifier of the location in the format `loc:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the location is
    mentioned.
    """

    name: List[object]
    """
    A span within the document's text representing the 'most proper' name of the
    location.

    As an example, a location referred to as 'New York City' in two places in a
    document, 'NYC' in three places, and 'the Big Apple' in one place would have its
    `name` set to whichever span the model was most confident represented the proper
    name of the location, likely being one of the 'New York City' spans.
    """

    parent: Optional[str] = None
    """
    A unique identifier for a location in the format `loc:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
    """

    type: Literal["country", "state", "city", "address", "other"]
    """
    The type of the location, being one of `country`, `state`, `city`, `address`, or
    `other`.
    """


class ResultDocumentPerson(BaseModel):
    """A legal person identified in a document."""

    id: str
    """
    The unique identifier of the person in the format `per:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
    """

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the person is
    mentioned.
    """

    name: List[object]
    """
    A span within the document's text representing the 'most proper' name of the
    person.

    As an example, a person referred to as 'Jonathan A. Doe' in two places in a
    document, 'John Doe' in three places, and 'Mr. Doe' in one place would have
    their `name` set to whichever span the model was most confident represented the
    proper name of the person, likely being one of the 'Jonathan A. Doe' spans.
    """

    parent: Optional[str] = None
    """
    A unique identifier for a legal person in the format `per:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    residence: Optional[str] = None
    """
    A unique identifier for a location in the format `loc:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
    """

    role: Literal[
        "plaintiff",
        "petitioner",
        "applicant",
        "appellant",
        "appellee",
        "claimant",
        "complainant",
        "defendant",
        "respondent",
        "prior_authority",
        "prosecutor",
        "defense_counsel",
        "amicus",
        "intervener",
        "borrower",
        "lender",
        "guarantor",
        "lessee",
        "lessor",
        "employer",
        "employee",
        "licensor",
        "licensee",
        "franchisor",
        "franchisee",
        "buyer",
        "seller",
        "contractor",
        "shareholder",
        "joint_venturer",
        "investor",
        "insurer",
        "insured",
        "enacting_authority",
        "empowered_authority",
        "settlor",
        "trustee",
        "beneficiary",
        "debater",
        "director",
        "governing_jurisdiction",
        "clerk",
        "witness",
        "other",
        "non_party",
    ]
    """The role of the person in relation to the subject of the document.

    The following roles are currently supported: | | | | ------------------------ |
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    | | `plaintiff` | A party initiating the case that is the subject of the
    document. | | `petitioner` | A party initiating the petition that is the subject
    of the document. | | `applicant` | A party initiating the application that is
    the subject of the document. | | `appellant` | A party appealing the decision
    that is the subject of the document. | | `appellee` | A party responding to the
    appeal that is the subject of the document if they are explicitly referred to as
    an 'appellee'. | | `claimant` | A party making a claim in the case that is the
    subject of the document. | | `complainant` | A party making a complaint in the
    case that is the subject of the document. | | `defendant` | A party defending
    against the case that is the subject of the document. | | `respondent` | A party
    responding to the petition, appeal, or application that is the subject of the
    document. | | `prior_authority` | An authority (e.g., judge, tribunal, court)
    that made a prior decision in the case that is the subject of the document. Both
    individual judges and courts should be annotated with this role where
    applicable. This is not to be used for authorities cited as precedent, only for
    those that made prior decisions in the same case. | | `prosecutor` | A lawyer
    prosecuting the case that is the subject of the document. | | `defense_counsel`
    | A lawyer defending the case that is the subject of the document. | | `amicus`
    | A party filing an amicus curiae brief in the case that is the subject of the
    document. | | `intervener` | A party attempting to or that has intervened in the
    case that is the subject of the document. | | `borrower` | A party borrowing
    money or other assets under the agreement that is the subject of the document,
    including 'mortgagors' and 'debtors'. | | `lender` | A party lending money or
    other assets under the agreement that is the subject of the document, including
    'mortgagees' and 'creditors'. | | `guarantor` | A party guaranteeing obligations
    under the agreement that is the subject of the document, including 'sureties'. |
    | `lessee` | A party leasing goods or services under the agreement that is the
    subject of the document, including 'tenants'. | | `lessor` | A party leasing
    goods or services under the agreement that is the subject of the document,
    including 'landlords'. | | `employer` | A party employing personnel under the
    agreement that is the subject of the document. | | `employee` | A party employed
    under the agreement that is the subject of the document. | | `licensor` | A
    party licensing intellectual property or other rights under the agreement that
    are the subject of the document. | | `licensee` | A party licensed to use
    intellectual property or other rights under the agreement that are the subject
    of the document. | | `franchisor` | A party granting a franchise under the
    agreement that is the subject of the document. | | `franchisee` | A party
    granted a franchise under the agreement that is the subject of the document. | |
    `buyer` | A party purchasing goods or services under the agreement that is the
    subject of the document, including 'purchasers', 'customers', and 'clients'. | |
    `seller` | A party selling or providing goods or services under the agreement
    that is the subject of the document, including 'Vendors', 'Suppliers', and
    'Service Providers' (where such parties are actually providing goods or services
    under the agreement). | | `contractor` | A party contracted to perform work or
    services under the agreement that is the subject of the document, including
    'consultants'. | | `shareholder` | A party holding shares or equity under the
    agreement that is the subject of the document. | | `joint_venturer` | A party
    participating in a joint venture under the agreement that is the subject of the
    document. | | `investor` | A party investing money or assets under the agreement
    that is the subject of the document. | | `insurer` | A party providing insurance
    under the agreement that is the subject of the document. | | `insured` | A party
    insured under the agreement that is the subject of the document. | | `settlor` |
    A party establishing the trust that is the subject of the document. | |
    `trustee` | A party managing the trust that is the subject of the document. | |
    `beneficiary` | A party benefiting from the trust that is the subject of the
    document. | | `enacting_authority` | An authority (e.g., legislature, regulator,
    Minister/Secretary, President/Prime Minister, tribunal, court, judge) giving
    legal effect to or authorizing the document. All relevant individuals and bodies
    should be annotated with this role where applicable. | | `empowered_authority` |
    An authority (e.g., government agency, regulator, Minister/Secretary,
    President/Prime Minister, tribunal, court) empowered by the document to carry
    out functions or duties. | | `debater` | A person participating in the debate
    that is the subject of the document. | | `governing_jurisdiction` | The
    jurisdiction whose laws govern the document. | | `director` | A director or
    other officer of a corporate legal person mentioned in the document. | | `clerk`
    | A clerk, notary, or other official certifying, witnessing, filing, recording,
    registering, or otherwise administering the document. | | `witness` | A witness
    witnessing the signing of the document, or whose testimony is part of the case
    that is the subject of the document. | | `other` | A party to the case,
    agreement, legislation, or regulation that is the subject of the document that
    does not fit into any of the other roles. | | `non_party` | A legal person
    mentioned in the document that is not a party to the case, agreement,
    legislation, or regulation that is the subject of the document. |
    """

    type: Literal["natural", "corporate", "politic"]
    """
    The legal entity type of the person, being one of `natural`, `corporate`, or
    `politic`.

    `natural` denotes a human being in their capacity as a natural legal person,
    including when representing unincorporated entities such as partnerships and
    trusts.

    `corporate` denotes a body corporate such as a company, incorporated
    partnership, or statutory corporation.

    `politic` denotes a body politic such as a court, state, government, or
    intergovernmental organization.
    """


class ResultDocumentPhoneNumber(BaseModel):
    """A valid phone number identified in a document belonging to a legal person.

    If a phone number was mentioned in the document but is not valid, possible, or attributable to a legal person, it will not be extracted.
    """

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the phone number
    is mentioned.
    """

    number: str
    """
    The normalized phone number in E.123 international notation conforming with
    local conventions on the use of spaces and hyphens as separators.
    """

    person: str
    """The unique identifier of the person that this phone number belongs to."""


class ResultDocumentQuote(BaseModel):
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

    span: List[object]
    """The span within the document's text where the quote occurs."""


class ResultDocumentSegment(BaseModel):
    """
    A segment within the document representing a structurally distinct portion of the document's content.
    """

    id: str
    """
    The unique identifier of the segment in the format `seg:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
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

    code: Optional[List[object]] = None
    """
    The start index and the index immediately after the end of a span of Unicode
    code points in input text.

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

    parent: Optional[str] = None
    """
    A unique identifier for a segment in the format `seg:{index}` where `{index}` is
    a non-negative incrementing integer starting from zero.
    """

    span: List[object]
    """The span of the segment within the document's text."""

    title: Optional[List[object]] = None
    """
    The start index and the index immediately after the end of a span of Unicode
    code points in input text.

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

    type_name: Optional[List[object]] = None
    """
    The start index and the index immediately after the end of a span of Unicode
    code points in input text.

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


class ResultDocumentTerm(BaseModel):
    """A term assigned a definite meaning within a document."""

    id: str
    """
    The unique identifier of the term in the format `term:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
    """

    meaning: List[object]
    """The span within the document's text providing the term's meaning or definition.

    For example, in the phrase '"Agreement" means this contract between the
    parties', the term's meaning would be the span covering 'this contract between
    the parties'.
    """

    mentions: List[List[object]]
    """
    An array of spans within the document's text where the term is mentioned outside
    of its definition.

    It is possible for the term to have no mentions if, outside of its definition,
    it is never referred to in the document.
    """

    name: List[object]
    """The span within the document's text defining the term's name.

    For example, in the phrase '"Agreement" means this contract between the
    parties', the term's name would be the span covering 'Agreement'.

    The term's name is different from and will never overlap with mentions of the
    term elsewhere in the document.
    """


class ResultDocumentWebsite(BaseModel):
    """A website identified in a document belonging to a legal person.

    If a website was mentioned in the document but is not attributable to a legal person, it will not be extracted.
    """

    mentions: List[List[object]]
    """
    An array of one or more spans within the document's text where the website is
    mentioned (including paths and slugs which are not part of the website's
    normalized URL).
    """

    person: str
    """The unique identifier of the person that this website belongs to."""

    url: str
    """The normalized URL of the website in the form `https://{host}/`."""


class ResultDocument(BaseModel):
    """The enriched document."""

    crossreferences: List[ResultDocumentCrossreference]
    """
    An array of cross-references within the document pointing to a single segment or
    a span of segments.
    """

    dates: List[ResultDocumentDate]
    """
    An array of dates identified in the document belonging to one of the following
    types: `creation`, `signature`, `effective`, `expiry`, `delivery`, `renewal`,
    `payment`, `birth`, or `death`.

    Only Gregorian dates between the years 1000 and 9999 (inclusive) fitting into
    one of the supported date types are extractable.
    """

    emails: List[ResultDocumentEmail]
    """
    An array of email addresses identified in the document belonging to legal
    persons.

    Email addresses mentioned in the document that are not attributable to legal
    persons will not be extracted.
    """

    external_documents: List[ResultDocumentExternalDocument]
    """An array of documents identified within the document."""

    headings: List[List[object]]
    """An array of spans within the document's text constituting headings."""

    id_numbers: List[ResultDocumentIDNumber]
    """
    An array of identification numbers identified in the document belonging to legal
    persons.

    Identification numbers mentioned in the document that are not attributable to
    legal persons will not be extracted.
    """

    junk: List[List[object]]
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

    locations: List[ResultDocumentLocation]
    """An array of locations identified in the document."""

    persons: List[ResultDocumentPerson]
    """An array of legal persons identified in the document."""

    phone_numbers: List[ResultDocumentPhoneNumber]
    """
    An array of valid phone numbers identified in the document belonging to legal
    persons.

    Phone numbers mentioned in the document that are not valid, possible, or
    attributable to legal persons will not be extracted.
    """

    quotes: List[ResultDocumentQuote]
    """An array of quotations within the document."""

    segments: List[ResultDocumentSegment]
    """
    An array of segments within the document representing structurally distinct
    portions of its content.
    """

    subtitle: Optional[List[object]] = None
    """
    The start index and the index immediately after the end of a span of Unicode
    code points in input text.

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

    terms: List[ResultDocumentTerm]
    """An array of terms assigned definite meanings within the document."""

    title: Optional[List[object]] = None
    """
    The start index and the index immediately after the end of a span of Unicode
    code points in input text.

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

    websites: List[ResultDocumentWebsite]
    """An array of websites identified in the document belonging to legal persons.

    Websites mentioned in the document that are not attributable to legal persons
    will not be extracted.
    """


class Result(BaseModel):
    """An enriched document alongside its index in the input array of texts."""

    document: ResultDocument
    """The enriched document."""

    index: int
    """
    The index of this document in the input array of texts, starting at `0` (and,
    therefore, ending at the number of inputs minus `1`).
    """


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
    space of the source document. Access to source documents is thus required to
    resolve spans into text.

    The first and second elements of a span correspond to the start index and the
    index immediately after the end of a span of Unicode code points.

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
