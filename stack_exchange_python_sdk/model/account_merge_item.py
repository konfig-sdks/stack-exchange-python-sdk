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


class AccountMergeItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            merge_date = schemas.IntSchema
            new_account_id = schemas.IntSchema
            old_account_id = schemas.IntSchema
            __annotations__ = {
                "merge_date": merge_date,
                "new_account_id": new_account_id,
                "old_account_id": old_account_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merge_date"]) -> MetaOapg.properties.merge_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_account_id"]) -> MetaOapg.properties.new_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["old_account_id"]) -> MetaOapg.properties.old_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["merge_date", "new_account_id", "old_account_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merge_date"]) -> typing.Union[MetaOapg.properties.merge_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_account_id"]) -> typing.Union[MetaOapg.properties.new_account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["old_account_id"]) -> typing.Union[MetaOapg.properties.old_account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["merge_date", "new_account_id", "old_account_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        merge_date: typing.Union[MetaOapg.properties.merge_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        new_account_id: typing.Union[MetaOapg.properties.new_account_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        old_account_id: typing.Union[MetaOapg.properties.old_account_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountMergeItem':
        return super().__new__(
            cls,
            *args,
            merge_date=merge_date,
            new_account_id=new_account_id,
            old_account_id=old_account_id,
            _configuration=_configuration,
            **kwargs,
        )
