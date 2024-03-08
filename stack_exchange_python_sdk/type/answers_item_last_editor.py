# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from stack_exchange_python_sdk.type.answers_item_last_editor_badge_counts import AnswersItemLastEditorBadgeCounts

class RequiredAnswersItemLastEditor(TypedDict):
    pass

class OptionalAnswersItemLastEditor(TypedDict, total=False):
    accept_rate: int

    badge_counts: AnswersItemLastEditorBadgeCounts

    display_name: str

    link: str

    profile_image: str

    reputation: int

    user_id: int

    user_type: str

class AnswersItemLastEditor(RequiredAnswersItemLastEditor, OptionalAnswersItemLastEditor):
    pass
