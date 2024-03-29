# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from stack_exchange_python_sdk.type.sites_item_aliases import SitesItemAliases
from stack_exchange_python_sdk.type.sites_item_markdown_extensions import SitesItemMarkdownExtensions
from stack_exchange_python_sdk.type.sites_item_related_sites import SitesItemRelatedSites
from stack_exchange_python_sdk.type.sites_item_styling import SitesItemStyling

class RequiredSitesItem(TypedDict):
    pass

class OptionalSitesItem(TypedDict, total=False):
    aliases: SitesItemAliases

    api_site_parameter: str

    audience: str

    closed_beta_date: int

    favicon_url: str

    high_resolution_icon_url: str

    icon_url: str

    launch_date: int

    logo_url: str

    markdown_extensions: SitesItemMarkdownExtensions

    name: str

    open_beta_date: int

    related_sites: SitesItemRelatedSites

    site_state: str

    site_type: str

    site_url: str

    styling: SitesItemStyling

    twitter_account: str

class SitesItem(RequiredSitesItem, OptionalSitesItem):
    pass
