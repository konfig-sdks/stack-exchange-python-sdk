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


class WritePermissionsItem(BaseModel):
    can_add: typing.Optional[bool] = Field(None, alias='can_add')

    can_delete: typing.Optional[bool] = Field(None, alias='can_delete')

    can_edit: typing.Optional[bool] = Field(None, alias='can_edit')

    max_daily_actions: typing.Optional[int] = Field(None, alias='max_daily_actions')

    min_seconds_between_actions: typing.Optional[int] = Field(None, alias='min_seconds_between_actions')

    object_type: typing.Optional[str] = Field(None, alias='object_type')

    user_id: typing.Optional[int] = Field(None, alias='user_id')
    class Config:
        arbitrary_types_allowed = True
