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

from stack_exchange_python_sdk.type.inbox_items_item_site import InboxItemsItemSite

class RequiredInboxItemsItem(TypedDict):
    pass

class OptionalInboxItemsItem(TypedDict, total=False):
    title: str

    answer_id: int

    body: str

    comment_id: int

    creation_date: int

    is_unread: bool

    item_type: str

    link: str

    question_id: int

    site: InboxItemsItemSite

class InboxItemsItem(RequiredInboxItemsItem, OptionalInboxItemsItem):
    pass
