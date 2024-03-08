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

from stack_exchange_python_sdk.type.created_comment_owner import CreatedCommentOwner
from stack_exchange_python_sdk.type.created_comment_reply_to_user import CreatedCommentReplyToUser

class RequiredCreatedComment(TypedDict):
    pass

class OptionalCreatedComment(TypedDict, total=False):
    body: str

    body_markdown: str

    can_flag: bool

    comment_id: int

    creation_date: int

    edited: bool

    link: str

    owner: CreatedCommentOwner

    post_id: int

    post_type: str

    reply_to_user: CreatedCommentReplyToUser

    score: int

    upvoted: bool

class CreatedComment(RequiredCreatedComment, OptionalCreatedComment):
    pass