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


class InboxItemsItemSiteStyling(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            link_color = schemas.StrSchema
            tag_background_color = schemas.StrSchema
            tag_foreground_color = schemas.StrSchema
            __annotations__ = {
                "link_color": link_color,
                "tag_background_color": tag_background_color,
                "tag_foreground_color": tag_foreground_color,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_color"]) -> MetaOapg.properties.link_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_background_color"]) -> MetaOapg.properties.tag_background_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_foreground_color"]) -> MetaOapg.properties.tag_foreground_color: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["link_color", "tag_background_color", "tag_foreground_color", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_color"]) -> typing.Union[MetaOapg.properties.link_color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_background_color"]) -> typing.Union[MetaOapg.properties.tag_background_color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_foreground_color"]) -> typing.Union[MetaOapg.properties.tag_foreground_color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["link_color", "tag_background_color", "tag_foreground_color", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        link_color: typing.Union[MetaOapg.properties.link_color, str, schemas.Unset] = schemas.unset,
        tag_background_color: typing.Union[MetaOapg.properties.tag_background_color, str, schemas.Unset] = schemas.unset,
        tag_foreground_color: typing.Union[MetaOapg.properties.tag_foreground_color, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InboxItemsItemSiteStyling':
        return super().__new__(
            cls,
            *args,
            link_color=link_color,
            tag_background_color=tag_background_color,
            tag_foreground_color=tag_foreground_color,
            _configuration=_configuration,
            **kwargs,
        )
