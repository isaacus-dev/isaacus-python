# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EnrichmentCreateParams"]


class EnrichmentCreateParams(TypedDict, total=False):
    model: Required[Literal["kanon-2-enricher"]]
    """
    The ID of the [model](https://docs.isaacus.com/models#enrichment) to use for
    enrichment.
    """

    texts: Required[Union[SequenceNotStr[str], str]]
    """
    A text or array of texts to be enriched, each containing at least one
    non-whitespace character.

    No more than 8 texts can be enriched in a single request.
    """

    overflow_strategy: Optional[Literal["auto", "drop_end"]]
    """The strategy for handling content exceeding the model's maximum input length.

    `auto` currently behaves the same as `drop_end`, dropping excess tokens from the
    end of input. In the future, `auto` may implement more sophisticated strategies
    such as chunking and context-aware stitching.

    `drop_end` drops tokens from the end of input exceeding the model's maximum
    input length.

    `null`, which is the default setting, raises an error if the input exceeds the
    model's maximum input length.
    """
