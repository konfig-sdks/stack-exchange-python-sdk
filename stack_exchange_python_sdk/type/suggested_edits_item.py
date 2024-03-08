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

from stack_exchange_python_sdk.type.suggested_edits_item_proposing_user import SuggestedEditsItemProposingUser
from stack_exchange_python_sdk.type.suggested_edits_item_tags import SuggestedEditsItemTags

class RequiredSuggestedEditsItem(TypedDict):
    pass

class OptionalSuggestedEditsItem(TypedDict, total=False):
    tags: SuggestedEditsItemTags

    title: str

    approval_date: int

    body: str

    comment: str

    creation_date: int

    post_id: int

    post_type: str

    proposing_user: SuggestedEditsItemProposingUser

    rejection_date: int

    suggested_edit_id: int

class SuggestedEditsItem(RequiredSuggestedEditsItem, OptionalSuggestedEditsItem):
    pass