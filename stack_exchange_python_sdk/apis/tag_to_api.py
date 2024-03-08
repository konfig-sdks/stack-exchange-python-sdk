import typing_extensions

from stack_exchange_python_sdk.apis.tags import TagValues
from stack_exchange_python_sdk.apis.tags.user_api import UserApi
from stack_exchange_python_sdk.apis.tags.answer_api import AnswerApi
from stack_exchange_python_sdk.apis.tags.tag_api import TagApi
from stack_exchange_python_sdk.apis.tags.question_api import QuestionApi
from stack_exchange_python_sdk.apis.tags.badge_api import BadgeApi
from stack_exchange_python_sdk.apis.tags.comment_api import CommentApi
from stack_exchange_python_sdk.apis.tags.post_api import PostApi
from stack_exchange_python_sdk.apis.tags.notification_api import NotificationApi
from stack_exchange_python_sdk.apis.tags.access_token_api import AccessTokenApi
from stack_exchange_python_sdk.apis.tags.message_api import MessageApi
from stack_exchange_python_sdk.apis.tags.reputation_api import ReputationApi
from stack_exchange_python_sdk.apis.tags.edit_api import EditApi
from stack_exchange_python_sdk.apis.tags.error_api import ErrorApi
from stack_exchange_python_sdk.apis.tags.filter_api import FilterApi
from stack_exchange_python_sdk.apis.tags.information_api import InformationApi
from stack_exchange_python_sdk.apis.tags.privilege_api import PrivilegeApi
from stack_exchange_python_sdk.apis.tags.query_api import QueryApi
from stack_exchange_python_sdk.apis.tags.event_api import EventApi
from stack_exchange_python_sdk.apis.tags.associated_api import AssociatedApi
from stack_exchange_python_sdk.apis.tags.favorite_api import FavoriteApi
from stack_exchange_python_sdk.apis.tags.mention_api import MentionApi
from stack_exchange_python_sdk.apis.tags.merge_api import MergeApi
from stack_exchange_python_sdk.apis.tags.timeline_api import TimelineApi
from stack_exchange_python_sdk.apis.tags.permission_api import PermissionApi
from stack_exchange_python_sdk.apis.tags.revision_api import RevisionApi
from stack_exchange_python_sdk.apis.tags.search_api import SearchApi
from stack_exchange_python_sdk.apis.tags.site_api import SiteApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USER: UserApi,
        TagValues.ANSWER: AnswerApi,
        TagValues.TAG: TagApi,
        TagValues.QUESTION: QuestionApi,
        TagValues.BADGE: BadgeApi,
        TagValues.COMMENT: CommentApi,
        TagValues.POST: PostApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ACCESS_TOKEN: AccessTokenApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.REPUTATION: ReputationApi,
        TagValues.EDIT: EditApi,
        TagValues.ERROR: ErrorApi,
        TagValues.FILTER: FilterApi,
        TagValues.INFORMATION: InformationApi,
        TagValues.PRIVILEGE: PrivilegeApi,
        TagValues.QUERY: QueryApi,
        TagValues.EVENT: EventApi,
        TagValues.ASSOCIATED: AssociatedApi,
        TagValues.FAVORITE: FavoriteApi,
        TagValues.MENTION: MentionApi,
        TagValues.MERGE: MergeApi,
        TagValues.TIMELINE: TimelineApi,
        TagValues.PERMISSION: PermissionApi,
        TagValues.REVISION: RevisionApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SITE: SiteApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USER: UserApi,
        TagValues.ANSWER: AnswerApi,
        TagValues.TAG: TagApi,
        TagValues.QUESTION: QuestionApi,
        TagValues.BADGE: BadgeApi,
        TagValues.COMMENT: CommentApi,
        TagValues.POST: PostApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ACCESS_TOKEN: AccessTokenApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.REPUTATION: ReputationApi,
        TagValues.EDIT: EditApi,
        TagValues.ERROR: ErrorApi,
        TagValues.FILTER: FilterApi,
        TagValues.INFORMATION: InformationApi,
        TagValues.PRIVILEGE: PrivilegeApi,
        TagValues.QUERY: QueryApi,
        TagValues.EVENT: EventApi,
        TagValues.ASSOCIATED: AssociatedApi,
        TagValues.FAVORITE: FavoriteApi,
        TagValues.MENTION: MentionApi,
        TagValues.MERGE: MergeApi,
        TagValues.TIMELINE: TimelineApi,
        TagValues.PERMISSION: PermissionApi,
        TagValues.REVISION: RevisionApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SITE: SiteApi,
    }
)
