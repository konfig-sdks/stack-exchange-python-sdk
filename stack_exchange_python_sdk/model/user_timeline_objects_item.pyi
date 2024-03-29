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


class UserTimelineObjectsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            badge_id = schemas.IntSchema
            comment_id = schemas.IntSchema
            creation_date = schemas.IntSchema
            detail = schemas.StrSchema
            link = schemas.StrSchema
            post_id = schemas.IntSchema
            post_type = schemas.StrSchema
            suggested_edit_id = schemas.IntSchema
            timeline_type = schemas.StrSchema
            user_id = schemas.IntSchema
            __annotations__ = {
                "title": title,
                "badge_id": badge_id,
                "comment_id": comment_id,
                "creation_date": creation_date,
                "detail": detail,
                "link": link,
                "post_id": post_id,
                "post_type": post_type,
                "suggested_edit_id": suggested_edit_id,
                "timeline_type": timeline_type,
                "user_id": user_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge_id"]) -> MetaOapg.properties.badge_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment_id"]) -> MetaOapg.properties.comment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_date"]) -> MetaOapg.properties.creation_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_id"]) -> MetaOapg.properties.post_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_type"]) -> MetaOapg.properties.post_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suggested_edit_id"]) -> MetaOapg.properties.suggested_edit_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeline_type"]) -> MetaOapg.properties.timeline_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "badge_id", "comment_id", "creation_date", "detail", "link", "post_id", "post_type", "suggested_edit_id", "timeline_type", "user_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge_id"]) -> typing.Union[MetaOapg.properties.badge_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment_id"]) -> typing.Union[MetaOapg.properties.comment_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_date"]) -> typing.Union[MetaOapg.properties.creation_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> typing.Union[MetaOapg.properties.detail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_id"]) -> typing.Union[MetaOapg.properties.post_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_type"]) -> typing.Union[MetaOapg.properties.post_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suggested_edit_id"]) -> typing.Union[MetaOapg.properties.suggested_edit_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeline_type"]) -> typing.Union[MetaOapg.properties.timeline_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "badge_id", "comment_id", "creation_date", "detail", "link", "post_id", "post_type", "suggested_edit_id", "timeline_type", "user_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        badge_id: typing.Union[MetaOapg.properties.badge_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        comment_id: typing.Union[MetaOapg.properties.comment_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creation_date: typing.Union[MetaOapg.properties.creation_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        detail: typing.Union[MetaOapg.properties.detail, str, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        post_id: typing.Union[MetaOapg.properties.post_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        post_type: typing.Union[MetaOapg.properties.post_type, str, schemas.Unset] = schemas.unset,
        suggested_edit_id: typing.Union[MetaOapg.properties.suggested_edit_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        timeline_type: typing.Union[MetaOapg.properties.timeline_type, str, schemas.Unset] = schemas.unset,
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserTimelineObjectsItem':
        return super().__new__(
            cls,
            *args,
            title=title,
            badge_id=badge_id,
            comment_id=comment_id,
            creation_date=creation_date,
            detail=detail,
            link=link,
            post_id=post_id,
            post_type=post_type,
            suggested_edit_id=suggested_edit_id,
            timeline_type=timeline_type,
            user_id=user_id,
            _configuration=_configuration,
            **kwargs,
        )
