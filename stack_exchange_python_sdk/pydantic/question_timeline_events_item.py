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

from stack_exchange_python_sdk.pydantic.question_timeline_events_item_owner import QuestionTimelineEventsItemOwner
from stack_exchange_python_sdk.pydantic.question_timeline_events_item_user import QuestionTimelineEventsItemUser

class QuestionTimelineEventsItem(BaseModel):
    comment_id: typing.Optional[int] = Field(None, alias='comment_id')

    creation_date: typing.Optional[int] = Field(None, alias='creation_date')

    down_vote_count: typing.Optional[int] = Field(None, alias='down_vote_count')

    owner: typing.Optional[QuestionTimelineEventsItemOwner] = Field(None, alias='owner')

    post_id: typing.Optional[int] = Field(None, alias='post_id')

    question_id: typing.Optional[int] = Field(None, alias='question_id')

    revision_guid: typing.Optional[str] = Field(None, alias='revision_guid')

    timeline_type: typing.Optional[str] = Field(None, alias='timeline_type')

    up_vote_count: typing.Optional[int] = Field(None, alias='up_vote_count')

    user: typing.Optional[QuestionTimelineEventsItemUser] = Field(None, alias='user')
    class Config:
        arbitrary_types_allowed = True
