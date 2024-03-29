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

from stack_exchange_python_sdk.type.info_object_site import InfoObjectSite

class RequiredInfoObject(TypedDict):
    pass

class OptionalInfoObject(TypedDict, total=False):
    answers_per_minute: typing.Union[int, float]

    api_revision: str

    badges_per_minute: typing.Union[int, float]

    new_active_users: int

    questions_per_minute: typing.Union[int, float]

    site: InfoObjectSite

    total_accepted: int

    total_answers: int

    total_badges: int

    total_comments: int

    total_questions: int

    total_unanswered: int

    total_users: int

    total_votes: int

class InfoObject(RequiredInfoObject, OptionalInfoObject):
    pass
