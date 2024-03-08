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


class QuestionsItemMigratedFromOtherSite(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def aliases() -> typing.Type['QuestionsItemMigratedFromOtherSiteAliases']:
                return QuestionsItemMigratedFromOtherSiteAliases
            api_site_parameter = schemas.StrSchema
            audience = schemas.StrSchema
            closed_beta_date = schemas.IntSchema
            favicon_url = schemas.StrSchema
            high_resolution_icon_url = schemas.StrSchema
            icon_url = schemas.StrSchema
            launch_date = schemas.IntSchema
            logo_url = schemas.StrSchema
        
            @staticmethod
            def markdown_extensions() -> typing.Type['QuestionsItemMigratedFromOtherSiteMarkdownExtensions']:
                return QuestionsItemMigratedFromOtherSiteMarkdownExtensions
            name = schemas.StrSchema
            open_beta_date = schemas.IntSchema
        
            @staticmethod
            def related_sites() -> typing.Type['QuestionsItemMigratedFromOtherSiteRelatedSites']:
                return QuestionsItemMigratedFromOtherSiteRelatedSites
            site_state = schemas.StrSchema
            site_type = schemas.StrSchema
            site_url = schemas.StrSchema
        
            @staticmethod
            def styling() -> typing.Type['QuestionsItemMigratedFromOtherSiteStyling']:
                return QuestionsItemMigratedFromOtherSiteStyling
            twitter_account = schemas.StrSchema
            __annotations__ = {
                "aliases": aliases,
                "api_site_parameter": api_site_parameter,
                "audience": audience,
                "closed_beta_date": closed_beta_date,
                "favicon_url": favicon_url,
                "high_resolution_icon_url": high_resolution_icon_url,
                "icon_url": icon_url,
                "launch_date": launch_date,
                "logo_url": logo_url,
                "markdown_extensions": markdown_extensions,
                "name": name,
                "open_beta_date": open_beta_date,
                "related_sites": related_sites,
                "site_state": site_state,
                "site_type": site_type,
                "site_url": site_url,
                "styling": styling,
                "twitter_account": twitter_account,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aliases"]) -> 'QuestionsItemMigratedFromOtherSiteAliases': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_site_parameter"]) -> MetaOapg.properties.api_site_parameter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience"]) -> MetaOapg.properties.audience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed_beta_date"]) -> MetaOapg.properties.closed_beta_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["favicon_url"]) -> MetaOapg.properties.favicon_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["high_resolution_icon_url"]) -> MetaOapg.properties.high_resolution_icon_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon_url"]) -> MetaOapg.properties.icon_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["launch_date"]) -> MetaOapg.properties.launch_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo_url"]) -> MetaOapg.properties.logo_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["markdown_extensions"]) -> 'QuestionsItemMigratedFromOtherSiteMarkdownExtensions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["open_beta_date"]) -> MetaOapg.properties.open_beta_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["related_sites"]) -> 'QuestionsItemMigratedFromOtherSiteRelatedSites': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_state"]) -> MetaOapg.properties.site_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_type"]) -> MetaOapg.properties.site_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_url"]) -> MetaOapg.properties.site_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["styling"]) -> 'QuestionsItemMigratedFromOtherSiteStyling': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twitter_account"]) -> MetaOapg.properties.twitter_account: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["aliases", "api_site_parameter", "audience", "closed_beta_date", "favicon_url", "high_resolution_icon_url", "icon_url", "launch_date", "logo_url", "markdown_extensions", "name", "open_beta_date", "related_sites", "site_state", "site_type", "site_url", "styling", "twitter_account", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aliases"]) -> typing.Union['QuestionsItemMigratedFromOtherSiteAliases', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_site_parameter"]) -> typing.Union[MetaOapg.properties.api_site_parameter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience"]) -> typing.Union[MetaOapg.properties.audience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed_beta_date"]) -> typing.Union[MetaOapg.properties.closed_beta_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["favicon_url"]) -> typing.Union[MetaOapg.properties.favicon_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["high_resolution_icon_url"]) -> typing.Union[MetaOapg.properties.high_resolution_icon_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon_url"]) -> typing.Union[MetaOapg.properties.icon_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["launch_date"]) -> typing.Union[MetaOapg.properties.launch_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo_url"]) -> typing.Union[MetaOapg.properties.logo_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["markdown_extensions"]) -> typing.Union['QuestionsItemMigratedFromOtherSiteMarkdownExtensions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["open_beta_date"]) -> typing.Union[MetaOapg.properties.open_beta_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["related_sites"]) -> typing.Union['QuestionsItemMigratedFromOtherSiteRelatedSites', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_state"]) -> typing.Union[MetaOapg.properties.site_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_type"]) -> typing.Union[MetaOapg.properties.site_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_url"]) -> typing.Union[MetaOapg.properties.site_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["styling"]) -> typing.Union['QuestionsItemMigratedFromOtherSiteStyling', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twitter_account"]) -> typing.Union[MetaOapg.properties.twitter_account, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["aliases", "api_site_parameter", "audience", "closed_beta_date", "favicon_url", "high_resolution_icon_url", "icon_url", "launch_date", "logo_url", "markdown_extensions", "name", "open_beta_date", "related_sites", "site_state", "site_type", "site_url", "styling", "twitter_account", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        aliases: typing.Union['QuestionsItemMigratedFromOtherSiteAliases', schemas.Unset] = schemas.unset,
        api_site_parameter: typing.Union[MetaOapg.properties.api_site_parameter, str, schemas.Unset] = schemas.unset,
        audience: typing.Union[MetaOapg.properties.audience, str, schemas.Unset] = schemas.unset,
        closed_beta_date: typing.Union[MetaOapg.properties.closed_beta_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        favicon_url: typing.Union[MetaOapg.properties.favicon_url, str, schemas.Unset] = schemas.unset,
        high_resolution_icon_url: typing.Union[MetaOapg.properties.high_resolution_icon_url, str, schemas.Unset] = schemas.unset,
        icon_url: typing.Union[MetaOapg.properties.icon_url, str, schemas.Unset] = schemas.unset,
        launch_date: typing.Union[MetaOapg.properties.launch_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        logo_url: typing.Union[MetaOapg.properties.logo_url, str, schemas.Unset] = schemas.unset,
        markdown_extensions: typing.Union['QuestionsItemMigratedFromOtherSiteMarkdownExtensions', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        open_beta_date: typing.Union[MetaOapg.properties.open_beta_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        related_sites: typing.Union['QuestionsItemMigratedFromOtherSiteRelatedSites', schemas.Unset] = schemas.unset,
        site_state: typing.Union[MetaOapg.properties.site_state, str, schemas.Unset] = schemas.unset,
        site_type: typing.Union[MetaOapg.properties.site_type, str, schemas.Unset] = schemas.unset,
        site_url: typing.Union[MetaOapg.properties.site_url, str, schemas.Unset] = schemas.unset,
        styling: typing.Union['QuestionsItemMigratedFromOtherSiteStyling', schemas.Unset] = schemas.unset,
        twitter_account: typing.Union[MetaOapg.properties.twitter_account, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'QuestionsItemMigratedFromOtherSite':
        return super().__new__(
            cls,
            *args,
            aliases=aliases,
            api_site_parameter=api_site_parameter,
            audience=audience,
            closed_beta_date=closed_beta_date,
            favicon_url=favicon_url,
            high_resolution_icon_url=high_resolution_icon_url,
            icon_url=icon_url,
            launch_date=launch_date,
            logo_url=logo_url,
            markdown_extensions=markdown_extensions,
            name=name,
            open_beta_date=open_beta_date,
            related_sites=related_sites,
            site_state=site_state,
            site_type=site_type,
            site_url=site_url,
            styling=styling,
            twitter_account=twitter_account,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.questions_item_migrated_from_other_site_aliases import QuestionsItemMigratedFromOtherSiteAliases
from stack_exchange_python_sdk.model.questions_item_migrated_from_other_site_markdown_extensions import QuestionsItemMigratedFromOtherSiteMarkdownExtensions
from stack_exchange_python_sdk.model.questions_item_migrated_from_other_site_related_sites import QuestionsItemMigratedFromOtherSiteRelatedSites
from stack_exchange_python_sdk.model.questions_item_migrated_from_other_site_styling import QuestionsItemMigratedFromOtherSiteStyling
