# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from stack_exchange_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from stack_exchange_python_sdk.api_response import AsyncGeneratorResponse
from stack_exchange_python_sdk import api_client, exceptions
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

from stack_exchange_python_sdk.model.notifications import Notifications as NotificationsSchema

from stack_exchange_python_sdk.type.notifications import Notifications

from ...api_client import Dictionary
from stack_exchange_python_sdk.pydantic.notifications import Notifications as NotificationsPydantic

# Query params
PagesizeSchema = schemas.IntSchema
PageSchema = schemas.IntSchema
FilterSchema = schemas.StrSchema
CallbackSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'pagesize': typing.Union[PagesizeSchema, decimal.Decimal, int, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'filter': typing.Union[FilterSchema, str, ],
        'callback': typing.Union[CallbackSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_pagesize = api_client.QueryParameter(
    name="pagesize",
    style=api_client.ParameterStyle.FORM,
    schema=PagesizeSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_param_callback = api_client.QueryParameter(
    name="callback",
    style=api_client.ParameterStyle.FORM,
    schema=CallbackSchema,
    explode=True,
)
SchemaFor200ResponseBody = NotificationsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Notifications


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Notifications


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        '*/*': api_client.MediaType(
            schema=SchemaFor200ResponseBody),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor402(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor402Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_402 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor402,
    response_cls_async=ApiResponseFor402Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
)


@dataclass
class ApiResponseFor406(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor406Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_406 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor406,
    response_cls_async=ApiResponseFor406Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)


@dataclass
class ApiResponseFor502(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor502Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_502 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor502,
    response_cls_async=ApiResponseFor502Async,
)


@dataclass
class ApiResponseFor503(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor503Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_503 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor503,
    response_cls_async=ApiResponseFor503Async,
)
_all_accept_content_types = (
    '*/*',
)


class BaseApi(api_client.Api):

    def _get_user_notifications_mapped_args(
        self,
        pagesize: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        param_callback: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if pagesize is not None:
            _query_params["pagesize"] = pagesize
        if page is not None:
            _query_params["page"] = page
        if filter is not None:
            _query_params["filter"] = filter
        if param_callback is not None:
            _query_params["callback"] = param_callback
        args.query = _query_params
        return args

    async def _aget_user_notifications_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pagesize,
            request_query_page,
            request_query_filter,
            request_query_param_callback,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/notifications',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_user_notifications_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pagesize,
            request_query_page,
            request_query_filter,
            request_query_param_callback,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/notifications',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetUserNotificationsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_notifications(
        self,
        pagesize: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        param_callback: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_notifications_mapped_args(
            pagesize=pagesize,
            page=page,
            filter=filter,
            param_callback=param_callback,
        )
        return await self._aget_user_notifications_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_user_notifications(
        self,
        pagesize: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        param_callback: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_notifications_mapped_args(
            pagesize=pagesize,
            page=page,
            filter=filter,
            param_callback=param_callback,
        )
        return self._get_user_notifications_oapg(
            query_params=args.query,
        )

class GetUserNotifications(BaseApi):

    async def aget_user_notifications(
        self,
        pagesize: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        param_callback: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> NotificationsPydantic:
        raw_response = await self.raw.aget_user_notifications(
            pagesize=pagesize,
            page=page,
            filter=filter,
            param_callback=param_callback,
            **kwargs,
        )
        if validate:
            return RootModel[NotificationsPydantic](raw_response.body).root
        return api_client.construct_model_instance(NotificationsPydantic, raw_response.body)
    
    
    def get_user_notifications(
        self,
        pagesize: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        param_callback: typing.Optional[str] = None,
        validate: bool = False,
    ) -> NotificationsPydantic:
        raw_response = self.raw.get_user_notifications(
            pagesize=pagesize,
            page=page,
            filter=filter,
            param_callback=param_callback,
        )
        if validate:
            return RootModel[NotificationsPydantic](raw_response.body).root
        return api_client.construct_model_instance(NotificationsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        pagesize: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        param_callback: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_notifications_mapped_args(
            pagesize=pagesize,
            page=page,
            filter=filter,
            param_callback=param_callback,
        )
        return await self._aget_user_notifications_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        pagesize: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        param_callback: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_notifications_mapped_args(
            pagesize=pagesize,
            page=page,
            filter=filter,
            param_callback=param_callback,
        )
        return self._get_user_notifications_oapg(
            query_params=args.query,
        )
