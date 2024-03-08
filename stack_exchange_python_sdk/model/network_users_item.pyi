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


class NetworkUsersItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            account_id = schemas.IntSchema
            answer_count = schemas.IntSchema
        
            @staticmethod
            def badge_counts() -> typing.Type['NetworkUsersItemBadgeCounts']:
                return NetworkUsersItemBadgeCounts
            creation_date = schemas.IntSchema
            last_access_date = schemas.IntSchema
            question_count = schemas.IntSchema
            reputation = schemas.IntSchema
            site_name = schemas.StrSchema
            site_url = schemas.StrSchema
        
            @staticmethod
            def top_answers() -> typing.Type['NetworkUsersItemTopAnswers']:
                return NetworkUsersItemTopAnswers
        
            @staticmethod
            def top_questions() -> typing.Type['NetworkUsersItemTopQuestions']:
                return NetworkUsersItemTopQuestions
            user_id = schemas.IntSchema
            user_type = schemas.StrSchema
            __annotations__ = {
                "account_id": account_id,
                "answer_count": answer_count,
                "badge_counts": badge_counts,
                "creation_date": creation_date,
                "last_access_date": last_access_date,
                "question_count": question_count,
                "reputation": reputation,
                "site_name": site_name,
                "site_url": site_url,
                "top_answers": top_answers,
                "top_questions": top_questions,
                "user_id": user_id,
                "user_type": user_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_count"]) -> MetaOapg.properties.answer_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge_counts"]) -> 'NetworkUsersItemBadgeCounts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_date"]) -> MetaOapg.properties.creation_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_access_date"]) -> MetaOapg.properties.last_access_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question_count"]) -> MetaOapg.properties.question_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reputation"]) -> MetaOapg.properties.reputation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_name"]) -> MetaOapg.properties.site_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_url"]) -> MetaOapg.properties.site_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top_answers"]) -> 'NetworkUsersItemTopAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top_questions"]) -> 'NetworkUsersItemTopQuestions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_type"]) -> MetaOapg.properties.user_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_id", "answer_count", "badge_counts", "creation_date", "last_access_date", "question_count", "reputation", "site_name", "site_url", "top_answers", "top_questions", "user_id", "user_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_count"]) -> typing.Union[MetaOapg.properties.answer_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge_counts"]) -> typing.Union['NetworkUsersItemBadgeCounts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_date"]) -> typing.Union[MetaOapg.properties.creation_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_access_date"]) -> typing.Union[MetaOapg.properties.last_access_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question_count"]) -> typing.Union[MetaOapg.properties.question_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reputation"]) -> typing.Union[MetaOapg.properties.reputation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_name"]) -> typing.Union[MetaOapg.properties.site_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_url"]) -> typing.Union[MetaOapg.properties.site_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["top_answers"]) -> typing.Union['NetworkUsersItemTopAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["top_questions"]) -> typing.Union['NetworkUsersItemTopQuestions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_type"]) -> typing.Union[MetaOapg.properties.user_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_id", "answer_count", "badge_counts", "creation_date", "last_access_date", "question_count", "reputation", "site_name", "site_url", "top_answers", "top_questions", "user_id", "user_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        account_id: typing.Union[MetaOapg.properties.account_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        answer_count: typing.Union[MetaOapg.properties.answer_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        badge_counts: typing.Union['NetworkUsersItemBadgeCounts', schemas.Unset] = schemas.unset,
        creation_date: typing.Union[MetaOapg.properties.creation_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_access_date: typing.Union[MetaOapg.properties.last_access_date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        question_count: typing.Union[MetaOapg.properties.question_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reputation: typing.Union[MetaOapg.properties.reputation, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        site_name: typing.Union[MetaOapg.properties.site_name, str, schemas.Unset] = schemas.unset,
        site_url: typing.Union[MetaOapg.properties.site_url, str, schemas.Unset] = schemas.unset,
        top_answers: typing.Union['NetworkUsersItemTopAnswers', schemas.Unset] = schemas.unset,
        top_questions: typing.Union['NetworkUsersItemTopQuestions', schemas.Unset] = schemas.unset,
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user_type: typing.Union[MetaOapg.properties.user_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NetworkUsersItem':
        return super().__new__(
            cls,
            *args,
            account_id=account_id,
            answer_count=answer_count,
            badge_counts=badge_counts,
            creation_date=creation_date,
            last_access_date=last_access_date,
            question_count=question_count,
            reputation=reputation,
            site_name=site_name,
            site_url=site_url,
            top_answers=top_answers,
            top_questions=top_questions,
            user_id=user_id,
            user_type=user_type,
            _configuration=_configuration,
            **kwargs,
        )

from stack_exchange_python_sdk.model.network_users_item_badge_counts import NetworkUsersItemBadgeCounts
from stack_exchange_python_sdk.model.network_users_item_top_answers import NetworkUsersItemTopAnswers
from stack_exchange_python_sdk.model.network_users_item_top_questions import NetworkUsersItemTopQuestions