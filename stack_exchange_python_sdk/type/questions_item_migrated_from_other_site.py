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

from stack_exchange_python_sdk.type.questions_item_migrated_from_other_site_aliases import QuestionsItemMigratedFromOtherSiteAliases
from stack_exchange_python_sdk.type.questions_item_migrated_from_other_site_markdown_extensions import QuestionsItemMigratedFromOtherSiteMarkdownExtensions
from stack_exchange_python_sdk.type.questions_item_migrated_from_other_site_related_sites import QuestionsItemMigratedFromOtherSiteRelatedSites
from stack_exchange_python_sdk.type.questions_item_migrated_from_other_site_styling import QuestionsItemMigratedFromOtherSiteStyling

class RequiredQuestionsItemMigratedFromOtherSite(TypedDict):
    pass

class OptionalQuestionsItemMigratedFromOtherSite(TypedDict, total=False):
    aliases: QuestionsItemMigratedFromOtherSiteAliases

    api_site_parameter: str

    audience: str

    closed_beta_date: int

    favicon_url: str

    high_resolution_icon_url: str

    icon_url: str

    launch_date: int

    logo_url: str

    markdown_extensions: QuestionsItemMigratedFromOtherSiteMarkdownExtensions

    name: str

    open_beta_date: int

    related_sites: QuestionsItemMigratedFromOtherSiteRelatedSites

    site_state: str

    site_type: str

    site_url: str

    styling: QuestionsItemMigratedFromOtherSiteStyling

    twitter_account: str

class QuestionsItemMigratedFromOtherSite(RequiredQuestionsItemMigratedFromOtherSite, OptionalQuestionsItemMigratedFromOtherSite):
    pass