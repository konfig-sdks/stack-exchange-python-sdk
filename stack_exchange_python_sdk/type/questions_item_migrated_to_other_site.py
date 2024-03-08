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

from stack_exchange_python_sdk.type.questions_item_migrated_to_other_site_aliases import QuestionsItemMigratedToOtherSiteAliases
from stack_exchange_python_sdk.type.questions_item_migrated_to_other_site_markdown_extensions import QuestionsItemMigratedToOtherSiteMarkdownExtensions
from stack_exchange_python_sdk.type.questions_item_migrated_to_other_site_related_sites import QuestionsItemMigratedToOtherSiteRelatedSites
from stack_exchange_python_sdk.type.questions_item_migrated_to_other_site_styling import QuestionsItemMigratedToOtherSiteStyling

class RequiredQuestionsItemMigratedToOtherSite(TypedDict):
    pass

class OptionalQuestionsItemMigratedToOtherSite(TypedDict, total=False):
    aliases: QuestionsItemMigratedToOtherSiteAliases

    api_site_parameter: str

    audience: str

    closed_beta_date: int

    favicon_url: str

    high_resolution_icon_url: str

    icon_url: str

    launch_date: int

    logo_url: str

    markdown_extensions: QuestionsItemMigratedToOtherSiteMarkdownExtensions

    name: str

    open_beta_date: int

    related_sites: QuestionsItemMigratedToOtherSiteRelatedSites

    site_state: str

    site_type: str

    site_url: str

    styling: QuestionsItemMigratedToOtherSiteStyling

    twitter_account: str

class QuestionsItemMigratedToOtherSite(RequiredQuestionsItemMigratedToOtherSite, OptionalQuestionsItemMigratedToOtherSite):
    pass
