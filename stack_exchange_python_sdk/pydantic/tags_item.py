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

from stack_exchange_python_sdk.pydantic.tags_item_synonyms import TagsItemSynonyms

class TagsItem(BaseModel):
    count: typing.Optional[int] = Field(None, alias='count')

    has_synonyms: typing.Optional[bool] = Field(None, alias='has_synonyms')

    is_moderator_only: typing.Optional[bool] = Field(None, alias='is_moderator_only')

    is_required: typing.Optional[bool] = Field(None, alias='is_required')

    last_activity_date: typing.Optional[int] = Field(None, alias='last_activity_date')

    name: typing.Optional[str] = Field(None, alias='name')

    synonyms: typing.Optional[TagsItemSynonyms] = Field(None, alias='synonyms')

    user_id: typing.Optional[int] = Field(None, alias='user_id')
    class Config:
        arbitrary_types_allowed = True
