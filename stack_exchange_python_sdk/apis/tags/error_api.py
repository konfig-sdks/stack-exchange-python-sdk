# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.errors_id.get import GenerateError
from stack_exchange_python_sdk.paths.errors.get import ListErrors
from stack_exchange_python_sdk.apis.tags.error_api_raw import ErrorApiRaw


class ErrorApi(
    GenerateError,
    ListErrors,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ErrorApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ErrorApiRaw(api_client)
