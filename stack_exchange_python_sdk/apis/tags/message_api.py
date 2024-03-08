# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.me_inbox.get import GetInboxItems
from stack_exchange_python_sdk.paths.inbox_unread.get import GetUnreadItems
from stack_exchange_python_sdk.paths.inbox.get import ListInboxItems
from stack_exchange_python_sdk.apis.tags.message_api_raw import MessageApiRaw


class MessageApi(
    GetInboxItems,
    GetUnreadItems,
    ListInboxItems,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MessageApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MessageApiRaw(api_client)
