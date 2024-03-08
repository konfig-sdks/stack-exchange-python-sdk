# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.posts_id_comments_add.post import AddComment
from stack_exchange_python_sdk.paths.posts_ids_comments.get import CommentsByIdsGet
from stack_exchange_python_sdk.paths.posts.get import GetAllPosts
from stack_exchange_python_sdk.paths.posts_ids_revisions.get import GetPostRevisionsByIds
from stack_exchange_python_sdk.paths.posts_ids.get import GetPostsByIds
from stack_exchange_python_sdk.paths.posts_ids_suggested_edits.get import ListSuggestedEdits
from stack_exchange_python_sdk.apis.tags.post_api_raw import PostApiRaw


class PostApi(
    AddComment,
    CommentsByIdsGet,
    GetAllPosts,
    GetPostRevisionsByIds,
    GetPostsByIds,
    ListSuggestedEdits,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PostApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PostApiRaw(api_client)
