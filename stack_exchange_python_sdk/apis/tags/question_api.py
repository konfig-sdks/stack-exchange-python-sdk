# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.questions.get import GetAllQuestions
from stack_exchange_python_sdk.paths.questions_ids.get import GetByIds
from stack_exchange_python_sdk.paths.questions_ids_linked.get import GetLinkedQuestions
from stack_exchange_python_sdk.paths.questions_ids_timeline.get import GetTimelineEvents
from stack_exchange_python_sdk.paths.me_questions_unaccepted.get import GetUnacceptedList
from stack_exchange_python_sdk.paths.me_questions_featured.get import GetUserFeatured
from stack_exchange_python_sdk.paths.me_questions.get import GetUserQuestionsList
from stack_exchange_python_sdk.paths.questions_featured.get import ListFeaturedQuestions
from stack_exchange_python_sdk.paths.questions_ids_related.get import ListRelatedQuestions
from stack_exchange_python_sdk.apis.tags.question_api_raw import QuestionApiRaw


class QuestionApi(
    GetAllQuestions,
    GetByIds,
    GetLinkedQuestions,
    GetTimelineEvents,
    GetUnacceptedList,
    GetUserFeatured,
    GetUserQuestionsList,
    ListFeaturedQuestions,
    ListRelatedQuestions,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: QuestionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = QuestionApiRaw(api_client)
