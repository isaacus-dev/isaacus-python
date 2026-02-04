# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .span import Span
from .._models import BaseModel

__all__ = ["Email"]


class Email(BaseModel):
    """An email address identified in a document belonging to a legal person.

    If an email address was mentioned in the document but is not attributable to a legal person, it will not be extracted.
    """

    address: str
    """The normalized email address."""

    person: str
    """The unique identifier of the person that this email address belongs to."""

    mentions: List[Span]
    """
    An array of one or more spans within the document's text where the email address
    is mentioned.
    """
