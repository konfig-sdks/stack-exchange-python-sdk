# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.me_suggested_edits.get import GetUserSuggestedEdits
from stack_exchange_python_sdk.paths.suggested_edits.get import ListSuggestedEdits
from stack_exchange_python_sdk.paths.suggested_edits_ids.get import ListSuggestedEdits0
from stack_exchange_python_sdk.apis.tags.edit_api_raw import EditApiRaw


class EditApi(
    GetUserSuggestedEdits,
    ListSuggestedEdits,
    ListSuggestedEdits0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EditApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EditApiRaw(api_client)
