# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .span import Span
from ...._models import BaseModel

__all__ = ["Person"]


class Person(BaseModel):
    """A legal person identified in a document."""

    id: str
    """
    The unique identifier of the person in the format `per:{index}` where `{index}`
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

    type: Literal["natural", "corporate", "politic"]
    """
    The legal entity type of the person, being one of `natural`, `corporate`, or
    `politic`.

    `natural` denotes a human being in their capacity as a natural legal person,
    including when representing unincorporated entities such as partnerships and
    trusts.

    `corporate` denotes a body corporate such as a company, incorporated
    partnership, or statutory corporation.

    `politic` denotes a body politic, political entity, or part thereof such as a
    court, state, government, or intergovernmental organization.
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

    parent: Optional[str] = None
    """
    A unique identifier for a legal person in the format `per:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    children: List[str]
    """
    The unique identifiers of any persons having this person as their immediate
    parent.
    """

    residence: Optional[str] = None
    """
    A unique identifier for a location in the format `loc:{index}` where `{index}`
    is a non-negative incrementing integer starting from zero.
    """

    mentions: List[Span]
    """
    An array of one or more spans within the document's text where the person is
    mentioned.
    """
