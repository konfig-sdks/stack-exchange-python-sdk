# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.me_merges.get import GetAccountMergeList
from stack_exchange_python_sdk.apis.tags.merge_api_raw import MergeApiRaw


class MergeApi(
    GetAccountMergeList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MergeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MergeApiRaw(api_client)
