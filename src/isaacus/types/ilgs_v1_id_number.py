# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .ilgs_v1_span import ILGSv1Span

__all__ = ["ILGSv1IDNumber"]


class ILGSv1IDNumber(BaseModel):
    """An identification number mentioned in a document belonging to a legal person.

    If an identification number was mentioned in the document but is not attributable to a legal person, it will not be extracted.
    """

    number: str
    """The identification number."""

    person: str
    """The unique identifier of the person that this identification number belongs to."""

    mentions: List[ILGSv1Span]
    """
    An array of one or more spans within the document's text where the
    identification number is mentioned.
    """
