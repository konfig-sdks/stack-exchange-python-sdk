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
from pydantic import BaseModel, Field, RootModel

from stack_exchange_python_sdk.pydantic.tag_score_objects_item_user_badge_counts import TagScoreObjectsItemUserBadgeCounts

class TagScoreObjectsItemUser(BaseModel):
    accept_rate: typing.Optional[int] = Field(None, alias='accept_rate')

    badge_counts: typing.Optional[TagScoreObjectsItemUserBadgeCounts] = Field(None, alias='badge_counts')

    display_name: typing.Optional[str] = Field(None, alias='display_name')

    link: typing.Optional[str] = Field(None, alias='link')

    profile_image: typing.Optional[str] = Field(None, alias='profile_image')

    reputation: typing.Optional[int] = Field(None, alias='reputation')

    user_id: typing.Optional[int] = Field(None, alias='user_id')

    user_type: typing.Optional[str] = Field(None, alias='user_type')
    class Config:
        arbitrary_types_allowed = True
