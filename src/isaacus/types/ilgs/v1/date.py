# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .span import Span
from ...._models import BaseModel

__all__ = ["Date"]


class Date(BaseModel):
    """
    A date identified in a document belonging to one of the following types: `creation`, `signature`, `effective`, `expiry`, `delivery`, `renewal`, `payment`, `birth`, or `death`.

    Only Gregorian dates between the years 1000 and 9999 (inclusive) fitting into one of the supported date types are extractable.
    """

    value: str
    """The date in ISO 8601 format (YYYY-MM-DD)."""

    type: Literal["creation", "signature", "effective", "expiry", "delivery", "renewal", "payment", "birth", "death"]
    """
    The type of the date, being one of `creation`, `signature`, `effective`,
    `expiry`, `delivery`, `renewal`, `payment`, `birth`, or `death`. If a date is
    mentioned in a document that does not fit into a supported type, it will not be
    extracted.

    `creation` denotes the date the document was created or last updated. There may
    only be one `creation` date per document.

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

    person: Optional[str] = None
    """
    A unique identifier for a legal person in the format `per:{index}` where
    `{index}` is a non-negative incrementing integer starting from zero.
    """

    mentions: List[Span]
    """
    An array of one or more spans within the document's text where the date is
    mentioned.
    """
