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


class TagWikisItemLastBodyEditor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            accept_rate = schemas.IntSchema
        
            @staticmethod
            def badge_counts() -> typing.Type['TagWikisItemLastBodyEditorBadgeCounts']:
                return TagWikisItemLastBodyEditorBadgeCounts
            display_name = schemas.StrSchema
            link = schemas.StrSchema
            profile_image = schemas.StrSchema
            reputation = schemas.IntSchema
            user_id = schemas.IntSchema
            user_type = schemas.StrSchema
            __annotations__ = {
                "accept_rate": accept_rate,
                "badge_counts": badge_counts,
                "display_name": display_name,
                "link": link,
                "profile_image": profile_image,
                "reputation": reputation,
                "user_id": user_id,
                "user_type": user_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accept_rate"]) -> MetaOapg.properties.accept_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge_counts"]) -> 'TagWikisItemLastBodyEditorBadgeCounts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile_image"]) -> MetaOapg.properties.profile_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reputation"]) -> MetaOapg.properties.reputation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_type"]) -> MetaOapg.properties.user_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accept_rate", "badge_counts", "display_name", "link", "profile_image", "reputation", "user_id", "user_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accept_rate"]) -> typing.Union[MetaOapg.properties.accept_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge_counts"]) -> typing.Union['TagWikisItemLastBodyEditorBadgeCounts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile_image"]) -> typing.Union[MetaOapg.properties.profile_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reputation"]) -> typing.Union[MetaOapg.properties.reputation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_type"]) -> typing.Union[MetaOapg.properties.user_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accept_rate", "badge_counts", "display_name", "link", "profile_image", "reputation", "user_id", "user_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accept_rate: typing.Union[MetaOapg.properties.accept_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        badge_counts: typing.Union['TagWikisItemLastBodyEditorBadgeCounts', schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        profile_image: typing.Union[MetaOapg.properties.profile_image, str, schemas.Unset] = schemas.unset,
        reputation: typing.Union[MetaOapg.properties.reputation, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user_type: typing.Union[MetaOapg.properties.user_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TagWikisItemLastBodyEditor':
        return super().__new__(
            cls,
            *args,
            accept_rate=accept_rate,
            badge_counts=badge_counts,
            display_name=display_name,
            link=link,
            profile_image=profile_image,
            reputation=reputation,
            user_id=user_id,
            user_type=user_type,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.tag_wikis_item_last_body_editor_badge_counts import TagWikisItemLastBodyEditorBadgeCounts
