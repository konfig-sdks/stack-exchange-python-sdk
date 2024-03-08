# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from stack_exchange_python_sdk import schemas  # noqa: F401


class TagSynonyms(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TagSynonymsItem']:
            return TagSynonymsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TagSynonymsItem'], typing.List['TagSynonymsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TagSynonyms':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TagSynonymsItem':
        return super().__getitem__(i)

from stack_exchange_python_sdk.model.tag_synonyms_item import TagSynonymsItem