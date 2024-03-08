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

from stack_exchange_python_sdk.pydantic.single_filter_included_fields import SingleFilterIncludedFields

class SingleFilter(BaseModel):
    filter: typing.Optional[str] = Field(None, alias='filter')

    filter_type: typing.Optional[str] = Field(None, alias='filter_type')

    included_fields: typing.Optional[SingleFilterIncludedFields] = Field(None, alias='included_fields')
    class Config:
        arbitrary_types_allowed = True
