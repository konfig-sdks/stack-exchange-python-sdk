# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.apps_access_tokens_de_authenticate.get import DeauthenticateListRaw
from stack_exchange_python_sdk.paths.access_tokens_access_tokens_invalidate.get import InvalidateListRaw
from stack_exchange_python_sdk.paths.access_tokens_access_tokens.get import ListPropertiesForMultipleTokensRaw


class AccessTokenApiRaw(
    DeauthenticateListRaw,
    InvalidateListRaw,
    ListPropertiesForMultipleTokensRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
