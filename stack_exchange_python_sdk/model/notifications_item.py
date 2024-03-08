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


class NotificationsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            body = schemas.StrSchema
            creation_date = schemas.IntSchema
            is_unread = schemas.BoolSchema
            notification_type = schemas.StrSchema
            post_id = schemas.IntSchema
        
            @staticmethod
            def site() -> typing.Type['NotificationsItemSite']:
                return NotificationsItemSite
            __annotations__ = {
                "body": body,
                "creation_date": creation_date,
                "is_unread": is_unread,
                "notification_type": notification_type,
                "post_id": post_id,
                "site": site,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_date"]) -> MetaOapg.properties.creation_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_unread"]) -> MetaOapg.properties.is_unread: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notification_type"]) -> MetaOapg.properties.notification_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_id"]) -> MetaOapg.properties.post_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site"]) -> 'NotificationsItemSite': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["body", "creation_date", "is_unread", "notification_type", "post_id", "site", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_date"]) -> typing.Union[MetaOapg.properties.creation_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_unread"]) -> typing.Union[MetaOapg.properties.is_unread, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notification_type"]) -> typing.Union[MetaOapg.properties.notification_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_id"]) -> typing.Union[MetaOapg.properties.post_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site"]) -> typing.Union['NotificationsItemSite', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["body", "creation_date", "is_unread", "notification_type", "post_id", "site", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        creation_date: typing.Union[MetaOapg.properties.creation_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_unread: typing.Union[MetaOapg.properties.is_unread, bool, schemas.Unset] = schemas.unset,
        notification_type: typing.Union[MetaOapg.properties.notification_type, str, schemas.Unset] = schemas.unset,
        post_id: typing.Union[MetaOapg.properties.post_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        site: typing.Union['NotificationsItemSite', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NotificationsItem':
        return super().__new__(
            cls,
            *args,
            body=body,
            creation_date=creation_date,
            is_unread=is_unread,
            notification_type=notification_type,
            post_id=post_id,
            site=site,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.notifications_item_site import NotificationsItemSite
