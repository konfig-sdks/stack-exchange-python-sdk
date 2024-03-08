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


class CreatedCommentOwnerBadgeCounts(BaseModel):
    bronze: typing.Optional[int] = Field(None, alias='bronze')

    gold: typing.Optional[int] = Field(None, alias='gold')

    silver: typing.Optional[int] = Field(None, alias='silver')
    class Config:
        arbitrary_types_allowed = True
