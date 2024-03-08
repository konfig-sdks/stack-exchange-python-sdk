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


RequiredEventsItem = TypedDict("RequiredEventsItem", {
    })

OptionalEventsItem = TypedDict("OptionalEventsItem", {
    "creation_date": int,

    "event_type": str,

    "excerpt": str,

    "link": str,

    "the id of the object (answer, comment, question, or user) the event describes": int,
    }, total=False)

class EventsItem(RequiredEventsItem, OptionalEventsItem):
    pass
