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


class RequiredSuggestedEditsItemProposingUserBadgeCounts(TypedDict):
    pass

class OptionalSuggestedEditsItemProposingUserBadgeCounts(TypedDict, total=False):
    bronze: int

    gold: int

    silver: int

class SuggestedEditsItemProposingUserBadgeCounts(RequiredSuggestedEditsItemProposingUserBadgeCounts, OptionalSuggestedEditsItemProposingUserBadgeCounts):
    pass
