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


class BadgesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            award_count = schemas.IntSchema
            badge_id = schemas.IntSchema
            badge_type = schemas.StrSchema
            link = schemas.StrSchema
            name = schemas.StrSchema
            rank = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['BadgesItemUser']:
                return BadgesItemUser
            __annotations__ = {
                "description": description,
                "award_count": award_count,
                "badge_id": badge_id,
                "badge_type": badge_type,
                "link": link,
                "name": name,
                "rank": rank,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["award_count"]) -> MetaOapg.properties.award_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge_id"]) -> MetaOapg.properties.badge_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge_type"]) -> MetaOapg.properties.badge_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'BadgesItemUser': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "award_count", "badge_id", "badge_type", "link", "name", "rank", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["award_count"]) -> typing.Union[MetaOapg.properties.award_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge_id"]) -> typing.Union[MetaOapg.properties.badge_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge_type"]) -> typing.Union[MetaOapg.properties.badge_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rank"]) -> typing.Union[MetaOapg.properties.rank, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['BadgesItemUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "award_count", "badge_id", "badge_type", "link", "name", "rank", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        award_count: typing.Union[MetaOapg.properties.award_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        badge_id: typing.Union[MetaOapg.properties.badge_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        badge_type: typing.Union[MetaOapg.properties.badge_type, str, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        rank: typing.Union[MetaOapg.properties.rank, str, schemas.Unset] = schemas.unset,
        user: typing.Union['BadgesItemUser', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BadgesItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            award_count=award_count,
            badge_id=badge_id,
            badge_type=badge_type,
            link=link,
            name=name,
            rank=rank,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.badges_item_user import BadgesItemUser
