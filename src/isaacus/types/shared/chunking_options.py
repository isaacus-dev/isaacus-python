# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ChunkingOptions"]


class ChunkingOptions(BaseModel):
    """Options for how to split text into smaller chunks."""

    size: Optional[int] = None
    """A whole number greater than or equal to 1."""

    overlap_ratio: Optional[float] = None
    """A number greater than or equal to 0 and less than 1."""

    overlap_tokens: Optional[int] = None
    """A whole number greater than or equal to 0."""
