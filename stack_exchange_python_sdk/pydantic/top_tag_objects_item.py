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


class TopTagObjectsItem(BaseModel):
    answer_count: typing.Optional[int] = Field(None, alias='answer_count')

    answer_score: typing.Optional[int] = Field(None, alias='answer_score')

    question_count: typing.Optional[int] = Field(None, alias='question_count')

    question_score: typing.Optional[int] = Field(None, alias='question_score')

    tag_name: typing.Optional[str] = Field(None, alias='tag_name')

    user_id: typing.Optional[int] = Field(None, alias='user_id')
    class Config:
        arbitrary_types_allowed = True
