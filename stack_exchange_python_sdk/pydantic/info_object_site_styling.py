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


class InfoObjectSiteStyling(BaseModel):
    link_color: typing.Optional[str] = Field(None, alias='link_color')

    tag_background_color: typing.Optional[str] = Field(None, alias='tag_background_color')

    tag_foreground_color: typing.Optional[str] = Field(None, alias='tag_foreground_color')
    class Config:
        arbitrary_types_allowed = True
