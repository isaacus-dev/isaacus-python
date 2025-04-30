# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["AnswerExtraction", "Extraction", "ExtractionAnswer", "Usage"]


class ExtractionAnswer(BaseModel):
    end: int
    """
    The index of the character immediately after the last character of the answer in
    the text, starting from `0` (such that, in Python, the answer is equivalent to
    `text[start:end]`).
    """

    score: float
    """
    A score between `0` and `1`, inclusive, representing the strength of the answer.
    """

    start: int
    """
    The index of the first character of the answer in the text, starting from `0`
    (and, therefore, ending at the number of characters in the text minus `1`).
    """

    text: str
    """The text of the answer."""


class Extraction(BaseModel):
    answers: List[ExtractionAnswer]
    """Answers extracted from the text, ordered from highest to lowest score."""

    index: int
    """
    The index of the text in the input array of texts that this result represents,
    starting from `0` (and, therefore, ending at the number of texts minus `1`).
    """

    inextractability_score: float
    """
    A score between `0` and `1`, inclusive, representing the likelihood that an
    answer can not be extracted from the text.

    Where this score is greater than the highest score of all possible answers, the
    text should be regarded as not having an extractable answer to the query. If
    that is the case and `ignore_inextractability` is `false`, no answers will be
    returned.
    """


class Usage(BaseModel):
    input_tokens: int
    """The number of tokens inputted to the model."""


class AnswerExtraction(BaseModel):
    extractions: List[Extraction]
    """
    The results of extracting answers from the texts, ordered from highest to lowest
    answer confidence score (or else lowest to highest inextractability score if
    there are no answers for a text).
    """

    usage: Usage
    """
    Statistics about the usage of resources in the process of extracting answers
    from the texts.
    """
