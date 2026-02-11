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

    overflow_strategy: Optional[Literal["auto", "drop_end", "chunk"]]
    """The strategy for handling content exceeding the model's maximum input length.

    `auto`, which is the default and recommended setting, currently behaves the same
    as `chunk`, which intelligently breaks the input up into smaller chunks and then
    stitches the results back together into a single prediction. In the future
    `auto` may implement even more sophisticated strategies for handling long
    contexts such as leveraging chunk overlap and/or a specialized stitching model.

    `chunk` breaks the input up into smaller chunks that fit within the model's
    context window and then intelligently merges the results into a single
    prediction at the cost of a minor accuracy drop.

    `drop_end` drops tokens from the end of input exceeding the model's maximum
    input length.

    `null`, which is the default setting, raises an error if the input exceeds the
    model's maximum input length.
    """
