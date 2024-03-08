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


class CreatedComment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            body = schemas.StrSchema
            body_markdown = schemas.StrSchema
            can_flag = schemas.BoolSchema
            comment_id = schemas.IntSchema
            creation_date = schemas.IntSchema
            edited = schemas.BoolSchema
            link = schemas.StrSchema
        
            @staticmethod
            def owner() -> typing.Type['CreatedCommentOwner']:
                return CreatedCommentOwner
            post_id = schemas.IntSchema
            post_type = schemas.StrSchema
        
            @staticmethod
            def reply_to_user() -> typing.Type['CreatedCommentReplyToUser']:
                return CreatedCommentReplyToUser
            score = schemas.IntSchema
            upvoted = schemas.BoolSchema
            __annotations__ = {
                "body": body,
                "body_markdown": body_markdown,
                "can_flag": can_flag,
                "comment_id": comment_id,
                "creation_date": creation_date,
                "edited": edited,
                "link": link,
                "owner": owner,
                "post_id": post_id,
                "post_type": post_type,
                "reply_to_user": reply_to_user,
                "score": score,
                "upvoted": upvoted,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_markdown"]) -> MetaOapg.properties.body_markdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_flag"]) -> MetaOapg.properties.can_flag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment_id"]) -> MetaOapg.properties.comment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_date"]) -> MetaOapg.properties.creation_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edited"]) -> MetaOapg.properties.edited: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> 'CreatedCommentOwner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_id"]) -> MetaOapg.properties.post_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_type"]) -> MetaOapg.properties.post_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_to_user"]) -> 'CreatedCommentReplyToUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upvoted"]) -> MetaOapg.properties.upvoted: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["body", "body_markdown", "can_flag", "comment_id", "creation_date", "edited", "link", "owner", "post_id", "post_type", "reply_to_user", "score", "upvoted", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_markdown"]) -> typing.Union[MetaOapg.properties.body_markdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_flag"]) -> typing.Union[MetaOapg.properties.can_flag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment_id"]) -> typing.Union[MetaOapg.properties.comment_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_date"]) -> typing.Union[MetaOapg.properties.creation_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edited"]) -> typing.Union[MetaOapg.properties.edited, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union['CreatedCommentOwner', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_id"]) -> typing.Union[MetaOapg.properties.post_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_type"]) -> typing.Union[MetaOapg.properties.post_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_to_user"]) -> typing.Union['CreatedCommentReplyToUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upvoted"]) -> typing.Union[MetaOapg.properties.upvoted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["body", "body_markdown", "can_flag", "comment_id", "creation_date", "edited", "link", "owner", "post_id", "post_type", "reply_to_user", "score", "upvoted", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        body_markdown: typing.Union[MetaOapg.properties.body_markdown, str, schemas.Unset] = schemas.unset,
        can_flag: typing.Union[MetaOapg.properties.can_flag, bool, schemas.Unset] = schemas.unset,
        comment_id: typing.Union[MetaOapg.properties.comment_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creation_date: typing.Union[MetaOapg.properties.creation_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        edited: typing.Union[MetaOapg.properties.edited, bool, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        owner: typing.Union['CreatedCommentOwner', schemas.Unset] = schemas.unset,
        post_id: typing.Union[MetaOapg.properties.post_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        post_type: typing.Union[MetaOapg.properties.post_type, str, schemas.Unset] = schemas.unset,
        reply_to_user: typing.Union['CreatedCommentReplyToUser', schemas.Unset] = schemas.unset,
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        upvoted: typing.Union[MetaOapg.properties.upvoted, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreatedComment':
        return super().__new__(
            cls,
            *args,
            body=body,
            body_markdown=body_markdown,
            can_flag=can_flag,
            comment_id=comment_id,
            creation_date=creation_date,
            edited=edited,
            link=link,
            owner=owner,
            post_id=post_id,
            post_type=post_type,
            reply_to_user=reply_to_user,
            score=score,
            upvoted=upvoted,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.created_comment_owner import CreatedCommentOwner
from stack_exchange_python_sdk.model.created_comment_reply_to_user import CreatedCommentReplyToUser
