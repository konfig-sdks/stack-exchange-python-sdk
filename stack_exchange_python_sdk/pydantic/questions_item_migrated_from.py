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

from stack_exchange_python_sdk.pydantic.questions_item_migrated_from_other_site import QuestionsItemMigratedFromOtherSite

class QuestionsItemMigratedFrom(BaseModel):
    on_date: typing.Optional[int] = Field(None, alias='on_date')

    other_site: typing.Optional[QuestionsItemMigratedFromOtherSite] = Field(None, alias='other_site')

    question_id: typing.Optional[int] = Field(None, alias='question_id')
    class Config:
        arbitrary_types_allowed = True