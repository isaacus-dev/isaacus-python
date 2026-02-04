# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ChunkingOptions"]


class ChunkingOptions(TypedDict, total=False):
    """Options for how to split text into smaller chunks."""

    size: Optional[int]
    """A whole number greater than or equal to 1."""

    overlap_ratio: Optional[float]
    """A number greater than or equal to 0 and less than 1."""

    overlap_tokens: Optional[int]
    """A whole number greater than or equal to 0."""
