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

from stack_exchange_python_sdk.type.posts_item_comments import PostsItemComments
from stack_exchange_python_sdk.type.posts_item_last_editor import PostsItemLastEditor
from stack_exchange_python_sdk.type.posts_item_owner import PostsItemOwner

class RequiredPostsItem(TypedDict):
    pass

class OptionalPostsItem(TypedDict, total=False):
    title: str

    body: str

    body_markdown: str

    comment_count: int

    comments: PostsItemComments

    creation_date: int

    down_vote_count: int

    downvoted: bool

    last_activity_date: int

    last_edit_date: int

    last_editor: PostsItemLastEditor

    link: str

    owner: PostsItemOwner

    post_id: int

    post_type: str

    score: int

    share_link: str

    up_vote_count: int

    upvoted: bool

class PostsItem(RequiredPostsItem, OptionalPostsItem):
    pass