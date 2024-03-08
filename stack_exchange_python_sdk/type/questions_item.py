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

from stack_exchange_python_sdk.type.questions_item_answers import QuestionsItemAnswers
from stack_exchange_python_sdk.type.questions_item_bounty_user import QuestionsItemBountyUser
from stack_exchange_python_sdk.type.questions_item_closed_details import QuestionsItemClosedDetails
from stack_exchange_python_sdk.type.questions_item_comments import QuestionsItemComments
from stack_exchange_python_sdk.type.questions_item_last_editor import QuestionsItemLastEditor
from stack_exchange_python_sdk.type.questions_item_migrated_from import QuestionsItemMigratedFrom
from stack_exchange_python_sdk.type.questions_item_migrated_to import QuestionsItemMigratedTo
from stack_exchange_python_sdk.type.questions_item_notice import QuestionsItemNotice
from stack_exchange_python_sdk.type.questions_item_owner import QuestionsItemOwner
from stack_exchange_python_sdk.type.questions_item_tags import QuestionsItemTags

class RequiredQuestionsItem(TypedDict):
    pass

class OptionalQuestionsItem(TypedDict, total=False):
    tags: QuestionsItemTags

    title: str

    accepted_answer_id: int

    answer_count: int

    answers: QuestionsItemAnswers

    body: str

    body_markdown: str

    bounty_amount: int

    bounty_closes_date: int

    bounty_user: QuestionsItemBountyUser

    can_close: bool

    can_flag: bool

    close_vote_count: int

    closed_date: int

    closed_details: QuestionsItemClosedDetails

    closed_reason: str

    comment_count: int

    comments: QuestionsItemComments

    community_owned_date: int

    creation_date: int

    delete_vote_count: int

    down_vote_count: int

    downvoted: bool

    favorite_count: int

    favorited: bool

    is_answered: bool

    last_activity_date: int

    last_edit_date: int

    last_editor: QuestionsItemLastEditor

    link: str

    locked_date: int

    migrated_from: QuestionsItemMigratedFrom

    migrated_to: QuestionsItemMigratedTo

    notice: QuestionsItemNotice

    owner: QuestionsItemOwner

    protected_date: int

    question_id: int

    reopen_vote_count: int

    score: int

    share_link: str

    up_vote_count: int

    upvoted: bool

    view_count: int

class QuestionsItem(RequiredQuestionsItem, OptionalQuestionsItem):
    pass
