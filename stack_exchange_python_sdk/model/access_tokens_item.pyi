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


class AccessTokensItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            access_token = schemas.StrSchema
            account_id = schemas.IntSchema
            expires_on_date = schemas.IntSchema
        
            @staticmethod
            def scope() -> typing.Type['AccessTokensItemScope']:
                return AccessTokensItemScope
            __annotations__ = {
                "access_token": access_token,
                "account_id": account_id,
                "expires_on_date": expires_on_date,
                "scope": scope,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_on_date"]) -> MetaOapg.properties.expires_on_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> 'AccessTokensItemScope': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access_token", "account_id", "expires_on_date", "scope", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token"]) -> typing.Union[MetaOapg.properties.access_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_on_date"]) -> typing.Union[MetaOapg.properties.expires_on_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union['AccessTokensItemScope', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access_token", "account_id", "expires_on_date", "scope", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access_token: typing.Union[MetaOapg.properties.access_token, str, schemas.Unset] = schemas.unset,
        account_id: typing.Union[MetaOapg.properties.account_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expires_on_date: typing.Union[MetaOapg.properties.expires_on_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        scope: typing.Union['AccessTokensItemScope', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessTokensItem':
        return super().__new__(
            cls,
            *args,
            access_token=access_token,
            account_id=account_id,
            expires_on_date=expires_on_date,
            scope=scope,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.access_tokens_item_scope import AccessTokensItemScope