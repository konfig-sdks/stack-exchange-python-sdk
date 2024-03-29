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

from stack_exchange_python_sdk.type.inbox_items_item_site_aliases import InboxItemsItemSiteAliases
from stack_exchange_python_sdk.type.inbox_items_item_site_markdown_extensions import InboxItemsItemSiteMarkdownExtensions
from stack_exchange_python_sdk.type.inbox_items_item_site_related_sites import InboxItemsItemSiteRelatedSites
from stack_exchange_python_sdk.type.inbox_items_item_site_styling import InboxItemsItemSiteStyling

class RequiredInboxItemsItemSite(TypedDict):
    pass

class OptionalInboxItemsItemSite(TypedDict, total=False):
    aliases: InboxItemsItemSiteAliases

    api_site_parameter: str

    audience: str

    closed_beta_date: int

    favicon_url: str

    high_resolution_icon_url: str

    icon_url: str

    launch_date: int

    logo_url: str

    markdown_extensions: InboxItemsItemSiteMarkdownExtensions

    name: str

    open_beta_date: int

    related_sites: InboxItemsItemSiteRelatedSites

    site_state: str

    site_type: str

    site_url: str

    styling: InboxItemsItemSiteStyling

    twitter_account: str

class InboxItemsItemSite(RequiredInboxItemsItemSite, OptionalInboxItemsItemSite):
    pass
