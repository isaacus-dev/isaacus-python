# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    model: Required[Literal["kanon-2-embedder"]]
    """
    The ID of the [model](https://docs.isaacus.com/models#embedding) to use for
    embedding.
    """

    texts: Required[Union[SequenceNotStr[str], str]]
    """The text or array of texts to embed.

    Each text must contain at least one non-whitespace character.

    No more than 128 texts can be embedded in a single request.
    """

    task: Optional[Literal["retrieval/query", "retrieval/document"]]
    """The task the embeddings will be used for.

    `retrieval/query` is meant for queries and statements, and `retrieval/document`
    is meant for anything to be retrieved using query embeddings.

    If `null`, which is the default setting, embeddings will not be optimized for
    any particular task.
    """

    overflow_strategy: Optional[Literal["drop_end"]]
    """The strategy to employ when content exceeds the model's maximum input length.

    `drop_end`, which is the default setting, drops tokens from the end of the
    content exceeding the limit.

    If `null`, an error will be raised if any content exceeds the model's maximum
    input length.
    """

    dimensions: Optional[int]
    """A whole number greater than or equal to 1."""
