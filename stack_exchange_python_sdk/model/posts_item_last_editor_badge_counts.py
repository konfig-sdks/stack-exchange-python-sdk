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


class PostsItemLastEditorBadgeCounts(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            bronze = schemas.IntSchema
            gold = schemas.IntSchema
            silver = schemas.IntSchema
            __annotations__ = {
                "bronze": bronze,
                "gold": gold,
                "silver": silver,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bronze"]) -> MetaOapg.properties.bronze: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gold"]) -> MetaOapg.properties.gold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["silver"]) -> MetaOapg.properties.silver: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bronze", "gold", "silver", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bronze"]) -> typing.Union[MetaOapg.properties.bronze, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gold"]) -> typing.Union[MetaOapg.properties.gold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["silver"]) -> typing.Union[MetaOapg.properties.silver, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bronze", "gold", "silver", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bronze: typing.Union[MetaOapg.properties.bronze, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        gold: typing.Union[MetaOapg.properties.gold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        silver: typing.Union[MetaOapg.properties.silver, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostsItemLastEditorBadgeCounts':
        return super().__new__(
            cls,
            *args,
            bronze=bronze,
            gold=gold,
            silver=silver,
            _configuration=_configuration,
            **kwargs,
        )
