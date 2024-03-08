# coding: utf-8

"""
    StackExchange

    Stack Exchange is a network of 130+ Q&A communities including Stack Overflow. 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from stack_exchange_python_sdk.paths.users_ids_associated.get import GetAssociatedAccounts
from stack_exchange_python_sdk.paths.users_ids_comments.get import GetCommentsByIds
from stack_exchange_python_sdk.paths.users_ids_favorites.get import GetFavoritesList
from stack_exchange_python_sdk.paths.users_ids_questions_featured.get import GetFeaturedQuestions
from stack_exchange_python_sdk.paths.users_id_reputation_history_full.get import GetFullReputationHistory
from stack_exchange_python_sdk.paths.users_id_inbox.get import GetInboxItems
from stack_exchange_python_sdk.paths.users_id_inbox_unread.get import GetInboxUnread
from stack_exchange_python_sdk.paths.users_id_notifications.get import GetNotificationsList
from stack_exchange_python_sdk.paths.users_id_privileges.get import GetPrivilegesList
from stack_exchange_python_sdk.paths.users_ids_questions.get import GetQuestionsByUserIds
from stack_exchange_python_sdk.paths.users_ids_reputation.get import GetReputationChanges
from stack_exchange_python_sdk.paths.users_ids_reputation_history.get import GetReputationHistory
from stack_exchange_python_sdk.paths.users_ids_suggested_edits.get import GetSuggestedEditsByIds
from stack_exchange_python_sdk.paths.users_ids_tags.get import GetTags
from stack_exchange_python_sdk.paths.users_id_top_question_tags.get import GetTopQuestionTags
from stack_exchange_python_sdk.paths.users_id_tags_tags_top_questions.get import GetTopQuestionsByTags
from stack_exchange_python_sdk.paths.users_ids_questions_unaccepted.get import GetUnacceptedQuestions
from stack_exchange_python_sdk.paths.users_ids_questions_unanswered.get import GetUnansweredQuestions
from stack_exchange_python_sdk.paths.users_id_notifications_unread.get import GetUnreadNotifications
from stack_exchange_python_sdk.paths.me.get import GetUser
from stack_exchange_python_sdk.paths.users_ids_answers.get import GetUserAnswersList
from stack_exchange_python_sdk.paths.users_ids_comments_toid.get import GetUserCommentsByIdsAndToid
from stack_exchange_python_sdk.paths.users_ids.get import GetUserProfilesByIds
from stack_exchange_python_sdk.paths.users_ids_timeline.get import GetUserTimelineByIds
from stack_exchange_python_sdk.paths.users_id_top_answer_tags.get import GetUserTopAnswerTags
from stack_exchange_python_sdk.paths.users_id_tags_tags_top_answers.get import GetUserTopAnswers
from stack_exchange_python_sdk.paths.users_id_write_permissions.get import GetWritePermissions
from stack_exchange_python_sdk.paths.users_ids_merges.get import ListAccountMerges
from stack_exchange_python_sdk.paths.users_moderators_elected.get import ListElectedModeratorUsers
from stack_exchange_python_sdk.paths.users_moderators.get import ListModeratorUsers
from stack_exchange_python_sdk.paths.users_ids_questions_no_answers.get import ListNoAnswerQuestions
from stack_exchange_python_sdk.paths.users_ids_badges.get import ListUserBadges
from stack_exchange_python_sdk.paths.users.get import ListUsers
from stack_exchange_python_sdk.paths.users_ids_mentioned.get import MentionedCommentsList
from stack_exchange_python_sdk.apis.tags.user_api_raw import UserApiRaw


class UserApi(
    GetAssociatedAccounts,
    GetCommentsByIds,
    GetFavoritesList,
    GetFeaturedQuestions,
    GetFullReputationHistory,
    GetInboxItems,
    GetInboxUnread,
    GetNotificationsList,
    GetPrivilegesList,
    GetQuestionsByUserIds,
    GetReputationChanges,
    GetReputationHistory,
    GetSuggestedEditsByIds,
    GetTags,
    GetTopQuestionTags,
    GetTopQuestionsByTags,
    GetUnacceptedQuestions,
    GetUnansweredQuestions,
    GetUnreadNotifications,
    GetUser,
    GetUserAnswersList,
    GetUserCommentsByIdsAndToid,
    GetUserProfilesByIds,
    GetUserTimelineByIds,
    GetUserTopAnswerTags,
    GetUserTopAnswers,
    GetWritePermissions,
    ListAccountMerges,
    ListElectedModeratorUsers,
    ListModeratorUsers,
    ListNoAnswerQuestions,
    ListUserBadges,
    ListUsers,
    MentionedCommentsList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UserApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UserApiRaw(api_client)
