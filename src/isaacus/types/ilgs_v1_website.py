# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .ilgs_v1_span import ILGSv1Span

__all__ = ["ILGSv1Website"]


class ILGSv1Website(BaseModel):
    """A website identified in a document belonging to a legal person.

    If a website was mentioned in the document but is not attributable to a legal person, it will not be extracted.
    """

    mentions: List[ILGSv1Span]
    """
    An array of one or more spans within the document's text where the website is
    mentioned (including paths and slugs which are not part of the website's
    normalized URL).
    """

    person: str
    """The unique identifier of the person that this website belongs to."""

    url: str
    """The normalized URL of the website in the form `https://{host}/`."""
