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


class QuestionsItemClosedDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def by_users() -> typing.Type['QuestionsItemClosedDetailsByUsers']:
                return QuestionsItemClosedDetailsByUsers
            on_hold = schemas.BoolSchema
        
            @staticmethod
            def original_questions() -> typing.Type['QuestionsItemClosedDetailsOriginalQuestions']:
                return QuestionsItemClosedDetailsOriginalQuestions
            reason = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "by_users": by_users,
                "on_hold": on_hold,
                "original_questions": original_questions,
                "reason": reason,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["by_users"]) -> 'QuestionsItemClosedDetailsByUsers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["on_hold"]) -> MetaOapg.properties.on_hold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_questions"]) -> 'QuestionsItemClosedDetailsOriginalQuestions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "by_users", "on_hold", "original_questions", "reason", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["by_users"]) -> typing.Union['QuestionsItemClosedDetailsByUsers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["on_hold"]) -> typing.Union[MetaOapg.properties.on_hold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_questions"]) -> typing.Union['QuestionsItemClosedDetailsOriginalQuestions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "by_users", "on_hold", "original_questions", "reason", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        by_users: typing.Union['QuestionsItemClosedDetailsByUsers', schemas.Unset] = schemas.unset,
        on_hold: typing.Union[MetaOapg.properties.on_hold, bool, schemas.Unset] = schemas.unset,
        original_questions: typing.Union['QuestionsItemClosedDetailsOriginalQuestions', schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'QuestionsItemClosedDetails':
        return super().__new__(
            cls,
            *args,
            description=description,
            by_users=by_users,
            on_hold=on_hold,
            original_questions=original_questions,
            reason=reason,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.questions_item_closed_details_by_users import QuestionsItemClosedDetailsByUsers
from stack_exchange_python_sdk.model.questions_item_closed_details_original_questions import QuestionsItemClosedDetailsOriginalQuestions
