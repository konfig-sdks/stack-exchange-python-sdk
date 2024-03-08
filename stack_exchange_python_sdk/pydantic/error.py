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


class Error(BaseModel):
    error_id: typing.Optional[typing.Union[int, float]] = Field(None, alias='error_id')

    error_message: typing.Optional[str] = Field(None, alias='error_message')

    error_name: typing.Optional[str] = Field(None, alias='error_name')
    class Config:
        arbitrary_types_allowed = True
