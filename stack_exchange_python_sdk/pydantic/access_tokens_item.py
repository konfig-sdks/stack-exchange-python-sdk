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

from stack_exchange_python_sdk.pydantic.access_tokens_item_scope import AccessTokensItemScope

class AccessTokensItem(BaseModel):
    access_token: typing.Optional[str] = Field(None, alias='access_token')

    account_id: typing.Optional[int] = Field(None, alias='account_id')

    expires_on_date: typing.Optional[int] = Field(None, alias='expires_on_date')

    scope: typing.Optional[AccessTokensItemScope] = Field(None, alias='scope')
    class Config:
        arbitrary_types_allowed = True
