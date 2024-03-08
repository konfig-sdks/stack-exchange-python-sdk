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

from stack_exchange_python_sdk.type.users_item_badge_counts import UsersItemBadgeCounts

class RequiredUsersItem(TypedDict):
    pass

class OptionalUsersItem(TypedDict, total=False):
    about_me: str

    accept_rate: int

    account_id: int

    age: int

    answer_count: int

    badge_counts: UsersItemBadgeCounts

    creation_date: int

    display_name: str

    down_vote_count: int

    is_employee: bool

    last_access_date: int

    last_modified_date: int

    link: str

    location: str

    profile_image: str

    question_count: int

    reputation: int

    reputation_change_day: int

    reputation_change_month: int

    reputation_change_quarter: int

    reputation_change_week: int

    reputation_change_year: int

    timed_penalty_date: int

    up_vote_count: int

    user_id: int

    user_type: str

    view_count: int

    website_url: str

class UsersItem(RequiredUsersItem, OptionalUsersItem):
    pass