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


class RevisionsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def tags() -> typing.Type['RevisionsItemTags']:
                return RevisionsItemTags
            title = schemas.StrSchema
            body = schemas.StrSchema
            comment = schemas.StrSchema
            creation_date = schemas.IntSchema
            is_rollback = schemas.BoolSchema
            last_body = schemas.StrSchema
        
            @staticmethod
            def last_tags() -> typing.Type['RevisionsItemLastTags']:
                return RevisionsItemLastTags
            last_title = schemas.StrSchema
            post_id = schemas.IntSchema
            post_type = schemas.StrSchema
            revision_guid = schemas.StrSchema
            revision_number = schemas.IntSchema
            revision_type = schemas.StrSchema
            set_community_wiki = schemas.BoolSchema
        
            @staticmethod
            def user() -> typing.Type['RevisionsItemUser']:
                return RevisionsItemUser
            __annotations__ = {
                "tags": tags,
                "title": title,
                "body": body,
                "comment": comment,
                "creation_date": creation_date,
                "is_rollback": is_rollback,
                "last_body": last_body,
                "last_tags": last_tags,
                "last_title": last_title,
                "post_id": post_id,
                "post_type": post_type,
                "revision_guid": revision_guid,
                "revision_number": revision_number,
                "revision_type": revision_type,
                "set_community_wiki": set_community_wiki,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'RevisionsItemTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_date"]) -> MetaOapg.properties.creation_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_rollback"]) -> MetaOapg.properties.is_rollback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_body"]) -> MetaOapg.properties.last_body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_tags"]) -> 'RevisionsItemLastTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_title"]) -> MetaOapg.properties.last_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_id"]) -> MetaOapg.properties.post_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_type"]) -> MetaOapg.properties.post_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revision_guid"]) -> MetaOapg.properties.revision_guid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revision_number"]) -> MetaOapg.properties.revision_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revision_type"]) -> MetaOapg.properties.revision_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["set_community_wiki"]) -> MetaOapg.properties.set_community_wiki: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'RevisionsItemUser': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "title", "body", "comment", "creation_date", "is_rollback", "last_body", "last_tags", "last_title", "post_id", "post_type", "revision_guid", "revision_number", "revision_type", "set_community_wiki", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['RevisionsItemTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_date"]) -> typing.Union[MetaOapg.properties.creation_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_rollback"]) -> typing.Union[MetaOapg.properties.is_rollback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_body"]) -> typing.Union[MetaOapg.properties.last_body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_tags"]) -> typing.Union['RevisionsItemLastTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_title"]) -> typing.Union[MetaOapg.properties.last_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_id"]) -> typing.Union[MetaOapg.properties.post_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_type"]) -> typing.Union[MetaOapg.properties.post_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revision_guid"]) -> typing.Union[MetaOapg.properties.revision_guid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revision_number"]) -> typing.Union[MetaOapg.properties.revision_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revision_type"]) -> typing.Union[MetaOapg.properties.revision_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["set_community_wiki"]) -> typing.Union[MetaOapg.properties.set_community_wiki, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['RevisionsItemUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "title", "body", "comment", "creation_date", "is_rollback", "last_body", "last_tags", "last_title", "post_id", "post_type", "revision_guid", "revision_number", "revision_type", "set_community_wiki", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union['RevisionsItemTags', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        creation_date: typing.Union[MetaOapg.properties.creation_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_rollback: typing.Union[MetaOapg.properties.is_rollback, bool, schemas.Unset] = schemas.unset,
        last_body: typing.Union[MetaOapg.properties.last_body, str, schemas.Unset] = schemas.unset,
        last_tags: typing.Union['RevisionsItemLastTags', schemas.Unset] = schemas.unset,
        last_title: typing.Union[MetaOapg.properties.last_title, str, schemas.Unset] = schemas.unset,
        post_id: typing.Union[MetaOapg.properties.post_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        post_type: typing.Union[MetaOapg.properties.post_type, str, schemas.Unset] = schemas.unset,
        revision_guid: typing.Union[MetaOapg.properties.revision_guid, str, schemas.Unset] = schemas.unset,
        revision_number: typing.Union[MetaOapg.properties.revision_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        revision_type: typing.Union[MetaOapg.properties.revision_type, str, schemas.Unset] = schemas.unset,
        set_community_wiki: typing.Union[MetaOapg.properties.set_community_wiki, bool, schemas.Unset] = schemas.unset,
        user: typing.Union['RevisionsItemUser', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RevisionsItem':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            title=title,
            body=body,
            comment=comment,
            creation_date=creation_date,
            is_rollback=is_rollback,
            last_body=last_body,
            last_tags=last_tags,
            last_title=last_title,
            post_id=post_id,
            post_type=post_type,
            revision_guid=revision_guid,
            revision_number=revision_number,
            revision_type=revision_type,
            set_community_wiki=set_community_wiki,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.revisions_item_last_tags import RevisionsItemLastTags
from stack_exchange_python_sdk.model.revisions_item_tags import RevisionsItemTags
from stack_exchange_python_sdk.model.revisions_item_user import RevisionsItemUser
