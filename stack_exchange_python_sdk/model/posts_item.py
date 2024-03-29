# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from stack_exchange_python_sdk import schemas  # noqa: F401


class PostsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            body = schemas.StrSchema
            body_markdown = schemas.StrSchema
            comment_count = schemas.IntSchema
        
            @staticmethod
            def comments() -> typing.Type['PostsItemComments']:
                return PostsItemComments
            creation_date = schemas.IntSchema
            down_vote_count = schemas.IntSchema
            downvoted = schemas.BoolSchema
            last_activity_date = schemas.IntSchema
            last_edit_date = schemas.IntSchema
        
            @staticmethod
            def last_editor() -> typing.Type['PostsItemLastEditor']:
                return PostsItemLastEditor
            link = schemas.StrSchema
        
            @staticmethod
            def owner() -> typing.Type['PostsItemOwner']:
                return PostsItemOwner
            post_id = schemas.IntSchema
            post_type = schemas.StrSchema
            score = schemas.IntSchema
            share_link = schemas.StrSchema
            up_vote_count = schemas.IntSchema
            upvoted = schemas.BoolSchema
            __annotations__ = {
                "title": title,
                "body": body,
                "body_markdown": body_markdown,
                "comment_count": comment_count,
                "comments": comments,
                "creation_date": creation_date,
                "down_vote_count": down_vote_count,
                "downvoted": downvoted,
                "last_activity_date": last_activity_date,
                "last_edit_date": last_edit_date,
                "last_editor": last_editor,
                "link": link,
                "owner": owner,
                "post_id": post_id,
                "post_type": post_type,
                "score": score,
                "share_link": share_link,
                "up_vote_count": up_vote_count,
                "upvoted": upvoted,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_markdown"]) -> MetaOapg.properties.body_markdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment_count"]) -> MetaOapg.properties.comment_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> 'PostsItemComments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_date"]) -> MetaOapg.properties.creation_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["down_vote_count"]) -> MetaOapg.properties.down_vote_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["downvoted"]) -> MetaOapg.properties.downvoted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_activity_date"]) -> MetaOapg.properties.last_activity_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_edit_date"]) -> MetaOapg.properties.last_edit_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_editor"]) -> 'PostsItemLastEditor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> 'PostsItemOwner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_id"]) -> MetaOapg.properties.post_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_type"]) -> MetaOapg.properties.post_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["share_link"]) -> MetaOapg.properties.share_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["up_vote_count"]) -> MetaOapg.properties.up_vote_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upvoted"]) -> MetaOapg.properties.upvoted: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "body", "body_markdown", "comment_count", "comments", "creation_date", "down_vote_count", "downvoted", "last_activity_date", "last_edit_date", "last_editor", "link", "owner", "post_id", "post_type", "score", "share_link", "up_vote_count", "upvoted", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_markdown"]) -> typing.Union[MetaOapg.properties.body_markdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment_count"]) -> typing.Union[MetaOapg.properties.comment_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union['PostsItemComments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_date"]) -> typing.Union[MetaOapg.properties.creation_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["down_vote_count"]) -> typing.Union[MetaOapg.properties.down_vote_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["downvoted"]) -> typing.Union[MetaOapg.properties.downvoted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_activity_date"]) -> typing.Union[MetaOapg.properties.last_activity_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_edit_date"]) -> typing.Union[MetaOapg.properties.last_edit_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_editor"]) -> typing.Union['PostsItemLastEditor', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union['PostsItemOwner', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_id"]) -> typing.Union[MetaOapg.properties.post_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_type"]) -> typing.Union[MetaOapg.properties.post_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["share_link"]) -> typing.Union[MetaOapg.properties.share_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["up_vote_count"]) -> typing.Union[MetaOapg.properties.up_vote_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upvoted"]) -> typing.Union[MetaOapg.properties.upvoted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "body", "body_markdown", "comment_count", "comments", "creation_date", "down_vote_count", "downvoted", "last_activity_date", "last_edit_date", "last_editor", "link", "owner", "post_id", "post_type", "score", "share_link", "up_vote_count", "upvoted", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        body_markdown: typing.Union[MetaOapg.properties.body_markdown, str, schemas.Unset] = schemas.unset,
        comment_count: typing.Union[MetaOapg.properties.comment_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        comments: typing.Union['PostsItemComments', schemas.Unset] = schemas.unset,
        creation_date: typing.Union[MetaOapg.properties.creation_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        down_vote_count: typing.Union[MetaOapg.properties.down_vote_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        downvoted: typing.Union[MetaOapg.properties.downvoted, bool, schemas.Unset] = schemas.unset,
        last_activity_date: typing.Union[MetaOapg.properties.last_activity_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_edit_date: typing.Union[MetaOapg.properties.last_edit_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_editor: typing.Union['PostsItemLastEditor', schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        owner: typing.Union['PostsItemOwner', schemas.Unset] = schemas.unset,
        post_id: typing.Union[MetaOapg.properties.post_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        post_type: typing.Union[MetaOapg.properties.post_type, str, schemas.Unset] = schemas.unset,
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        share_link: typing.Union[MetaOapg.properties.share_link, str, schemas.Unset] = schemas.unset,
        up_vote_count: typing.Union[MetaOapg.properties.up_vote_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        upvoted: typing.Union[MetaOapg.properties.upvoted, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostsItem':
        return super().__new__(
            cls,
            *args,
            title=title,
            body=body,
            body_markdown=body_markdown,
            comment_count=comment_count,
            comments=comments,
            creation_date=creation_date,
            down_vote_count=down_vote_count,
            downvoted=downvoted,
            last_activity_date=last_activity_date,
            last_edit_date=last_edit_date,
            last_editor=last_editor,
            link=link,
            owner=owner,
            post_id=post_id,
            post_type=post_type,
            score=score,
            share_link=share_link,
            up_vote_count=up_vote_count,
            upvoted=upvoted,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.posts_item_comments import PostsItemComments
from stack_exchange_python_sdk.model.posts_item_last_editor import PostsItemLastEditor
from stack_exchange_python_sdk.model.posts_item_owner import PostsItemOwner
