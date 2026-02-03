# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .ilgs_v1_span import ILGSv1Span

__all__ = ["ILGSv1PhoneNumber"]


class ILGSv1PhoneNumber(BaseModel):
    """A valid phone number identified in a document belonging to a legal person.

    If a phone number was mentioned in the document but is not valid, possible, or attributable to a legal person, it will not be extracted.
    """

    number: str
    """
    The normalized phone number in E.123 international notation conforming with
    local conventions on the use of spaces and hyphens as separators.
    """

    person: str
    """The unique identifier of the person that this phone number belongs to."""

    mentions: List[ILGSv1Span]
    """
    An array of one or more spans within the document's text where the phone number
    is mentioned.
    """
