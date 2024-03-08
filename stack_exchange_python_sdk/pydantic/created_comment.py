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

from stack_exchange_python_sdk.pydantic.created_comment_owner import CreatedCommentOwner
from stack_exchange_python_sdk.pydantic.created_comment_reply_to_user import CreatedCommentReplyToUser

class CreatedComment(BaseModel):
    body: typing.Optional[str] = Field(None, alias='body')

    body_markdown: typing.Optional[str] = Field(None, alias='body_markdown')

    can_flag: typing.Optional[bool] = Field(None, alias='can_flag')

    comment_id: typing.Optional[int] = Field(None, alias='comment_id')

    creation_date: typing.Optional[int] = Field(None, alias='creation_date')

    edited: typing.Optional[bool] = Field(None, alias='edited')

    link: typing.Optional[str] = Field(None, alias='link')

    owner: typing.Optional[CreatedCommentOwner] = Field(None, alias='owner')

    post_id: typing.Optional[int] = Field(None, alias='post_id')

    post_type: typing.Optional[str] = Field(None, alias='post_type')

    reply_to_user: typing.Optional[CreatedCommentReplyToUser] = Field(None, alias='reply_to_user')

    score: typing.Optional[int] = Field(None, alias='score')

    upvoted: typing.Optional[bool] = Field(None, alias='upvoted')
    class Config:
        arbitrary_types_allowed = True