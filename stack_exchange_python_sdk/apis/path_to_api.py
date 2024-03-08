import typing_extensions

from stack_exchange_python_sdk.paths import PathValues
from stack_exchange_python_sdk.apis.paths.access_tokens_access_tokens import AccessTokensAccessTokens
from stack_exchange_python_sdk.apis.paths.access_tokens_access_tokens_invalidate import AccessTokensAccessTokensInvalidate
from stack_exchange_python_sdk.apis.paths.answers import Answers
from stack_exchange_python_sdk.apis.paths.answers_ids import AnswersIds
from stack_exchange_python_sdk.apis.paths.answers_ids_comments import AnswersIdsComments
from stack_exchange_python_sdk.apis.paths.apps_access_tokens_de_authenticate import AppsAccessTokensDeAuthenticate
from stack_exchange_python_sdk.apis.paths.badges import Badges
from stack_exchange_python_sdk.apis.paths.badges_name import BadgesName
from stack_exchange_python_sdk.apis.paths.badges_recipients import BadgesRecipients
from stack_exchange_python_sdk.apis.paths.badges_tags import BadgesTags
from stack_exchange_python_sdk.apis.paths.badges_ids import BadgesIds
from stack_exchange_python_sdk.apis.paths.badges_ids_recipients import BadgesIdsRecipients
from stack_exchange_python_sdk.apis.paths.comments import Comments
from stack_exchange_python_sdk.apis.paths.comments_ids import CommentsIds
from stack_exchange_python_sdk.apis.paths.comments_id_delete import CommentsIdDelete
from stack_exchange_python_sdk.apis.paths.comments_id_edit import CommentsIdEdit
from stack_exchange_python_sdk.apis.paths.errors import Errors
from stack_exchange_python_sdk.apis.paths.errors_id import ErrorsId
from stack_exchange_python_sdk.apis.paths.events import Events
from stack_exchange_python_sdk.apis.paths.filters_create import FiltersCreate
from stack_exchange_python_sdk.apis.paths.filters_filters import FiltersFilters
from stack_exchange_python_sdk.apis.paths.inbox import Inbox
from stack_exchange_python_sdk.apis.paths.inbox_unread import InboxUnread
from stack_exchange_python_sdk.apis.paths.info import Info
from stack_exchange_python_sdk.apis.paths.me import Me
from stack_exchange_python_sdk.apis.paths.me_answers import MeAnswers
from stack_exchange_python_sdk.apis.paths.me_associated import MeAssociated
from stack_exchange_python_sdk.apis.paths.me_badges import MeBadges
from stack_exchange_python_sdk.apis.paths.me_comments import MeComments
from stack_exchange_python_sdk.apis.paths.me_comments_to_id import MeCommentsToId
from stack_exchange_python_sdk.apis.paths.me_favorites import MeFavorites
from stack_exchange_python_sdk.apis.paths.me_inbox import MeInbox
from stack_exchange_python_sdk.apis.paths.me_inbox_unread import MeInboxUnread
from stack_exchange_python_sdk.apis.paths.me_mentioned import MeMentioned
from stack_exchange_python_sdk.apis.paths.me_merges import MeMerges
from stack_exchange_python_sdk.apis.paths.me_notifications import MeNotifications
from stack_exchange_python_sdk.apis.paths.me_notifications_unread import MeNotificationsUnread
from stack_exchange_python_sdk.apis.paths.me_privileges import MePrivileges
from stack_exchange_python_sdk.apis.paths.me_questions import MeQuestions
from stack_exchange_python_sdk.apis.paths.me_questions_featured import MeQuestionsFeatured
from stack_exchange_python_sdk.apis.paths.me_questions_no_answers import MeQuestionsNoAnswers
from stack_exchange_python_sdk.apis.paths.me_questions_unaccepted import MeQuestionsUnaccepted
from stack_exchange_python_sdk.apis.paths.me_questions_unanswered import MeQuestionsUnanswered
from stack_exchange_python_sdk.apis.paths.me_reputation import MeReputation
from stack_exchange_python_sdk.apis.paths.me_reputation_history import MeReputationHistory
from stack_exchange_python_sdk.apis.paths.me_reputation_history_full import MeReputationHistoryFull
from stack_exchange_python_sdk.apis.paths.me_suggested_edits import MeSuggestedEdits
from stack_exchange_python_sdk.apis.paths.me_tags import MeTags
from stack_exchange_python_sdk.apis.paths.me_tags_tags_top_answers import MeTagsTagsTopAnswers
from stack_exchange_python_sdk.apis.paths.me_tags_tags_top_questions import MeTagsTagsTopQuestions
from stack_exchange_python_sdk.apis.paths.me_timeline import MeTimeline
from stack_exchange_python_sdk.apis.paths.me_top_answer_tags import MeTopAnswerTags
from stack_exchange_python_sdk.apis.paths.me_top_question_tags import MeTopQuestionTags
from stack_exchange_python_sdk.apis.paths.me_write_permissions import MeWritePermissions
from stack_exchange_python_sdk.apis.paths.notifications import Notifications
from stack_exchange_python_sdk.apis.paths.notifications_unread import NotificationsUnread
from stack_exchange_python_sdk.apis.paths.posts import Posts
from stack_exchange_python_sdk.apis.paths.posts_ids import PostsIds
from stack_exchange_python_sdk.apis.paths.posts_ids_comments import PostsIdsComments
from stack_exchange_python_sdk.apis.paths.posts_ids_revisions import PostsIdsRevisions
from stack_exchange_python_sdk.apis.paths.posts_ids_suggested_edits import PostsIdsSuggestedEdits
from stack_exchange_python_sdk.apis.paths.posts_id_comments_add import PostsIdCommentsAdd
from stack_exchange_python_sdk.apis.paths.privileges import Privileges
from stack_exchange_python_sdk.apis.paths.questions import Questions
from stack_exchange_python_sdk.apis.paths.questions_featured import QuestionsFeatured
from stack_exchange_python_sdk.apis.paths.questions_no_answers import QuestionsNoAnswers
from stack_exchange_python_sdk.apis.paths.questions_unanswered import QuestionsUnanswered
from stack_exchange_python_sdk.apis.paths.questions_ids import QuestionsIds
from stack_exchange_python_sdk.apis.paths.questions_ids_answers import QuestionsIdsAnswers
from stack_exchange_python_sdk.apis.paths.questions_ids_comments import QuestionsIdsComments
from stack_exchange_python_sdk.apis.paths.questions_ids_linked import QuestionsIdsLinked
from stack_exchange_python_sdk.apis.paths.questions_ids_related import QuestionsIdsRelated
from stack_exchange_python_sdk.apis.paths.questions_ids_timeline import QuestionsIdsTimeline
from stack_exchange_python_sdk.apis.paths.revisions_ids import RevisionsIds
from stack_exchange_python_sdk.apis.paths.search import Search
from stack_exchange_python_sdk.apis.paths.search_advanced import SearchAdvanced
from stack_exchange_python_sdk.apis.paths.similar import Similar
from stack_exchange_python_sdk.apis.paths.sites import Sites
from stack_exchange_python_sdk.apis.paths.suggested_edits import SuggestedEdits
from stack_exchange_python_sdk.apis.paths.suggested_edits_ids import SuggestedEditsIds
from stack_exchange_python_sdk.apis.paths.tags import Tags
from stack_exchange_python_sdk.apis.paths.tags_moderator_only import TagsModeratorOnly
from stack_exchange_python_sdk.apis.paths.tags_required import TagsRequired
from stack_exchange_python_sdk.apis.paths.tags_synonyms import TagsSynonyms
from stack_exchange_python_sdk.apis.paths.tags_tags_faq import TagsTagsFaq
from stack_exchange_python_sdk.apis.paths.tags_tags_info import TagsTagsInfo
from stack_exchange_python_sdk.apis.paths.tags_tags_related import TagsTagsRelated
from stack_exchange_python_sdk.apis.paths.tags_tags_synonyms import TagsTagsSynonyms
from stack_exchange_python_sdk.apis.paths.tags_tags_wikis import TagsTagsWikis
from stack_exchange_python_sdk.apis.paths.tags_tag_top_answerers_period import TagsTagTopAnswerersPeriod
from stack_exchange_python_sdk.apis.paths.tags_tag_top_askers_period import TagsTagTopAskersPeriod
from stack_exchange_python_sdk.apis.paths.users import Users
from stack_exchange_python_sdk.apis.paths.users_moderators import UsersModerators
from stack_exchange_python_sdk.apis.paths.users_moderators_elected import UsersModeratorsElected
from stack_exchange_python_sdk.apis.paths.users_ids import UsersIds
from stack_exchange_python_sdk.apis.paths.users_ids_answers import UsersIdsAnswers
from stack_exchange_python_sdk.apis.paths.users_ids_associated import UsersIdsAssociated
from stack_exchange_python_sdk.apis.paths.users_ids_badges import UsersIdsBadges
from stack_exchange_python_sdk.apis.paths.users_ids_comments import UsersIdsComments
from stack_exchange_python_sdk.apis.paths.users_ids_comments_toid import UsersIdsCommentsToid
from stack_exchange_python_sdk.apis.paths.users_ids_favorites import UsersIdsFavorites
from stack_exchange_python_sdk.apis.paths.users_ids_mentioned import UsersIdsMentioned
from stack_exchange_python_sdk.apis.paths.users_ids_merges import UsersIdsMerges
from stack_exchange_python_sdk.apis.paths.users_ids_questions import UsersIdsQuestions
from stack_exchange_python_sdk.apis.paths.users_ids_questions_featured import UsersIdsQuestionsFeatured
from stack_exchange_python_sdk.apis.paths.users_ids_questions_no_answers import UsersIdsQuestionsNoAnswers
from stack_exchange_python_sdk.apis.paths.users_ids_questions_unaccepted import UsersIdsQuestionsUnaccepted
from stack_exchange_python_sdk.apis.paths.users_ids_questions_unanswered import UsersIdsQuestionsUnanswered
from stack_exchange_python_sdk.apis.paths.users_ids_reputation import UsersIdsReputation
from stack_exchange_python_sdk.apis.paths.users_ids_reputation_history import UsersIdsReputationHistory
from stack_exchange_python_sdk.apis.paths.users_ids_suggested_edits import UsersIdsSuggestedEdits
from stack_exchange_python_sdk.apis.paths.users_ids_tags import UsersIdsTags
from stack_exchange_python_sdk.apis.paths.users_ids_timeline import UsersIdsTimeline
from stack_exchange_python_sdk.apis.paths.users_id_inbox import UsersIdInbox
from stack_exchange_python_sdk.apis.paths.users_id_inbox_unread import UsersIdInboxUnread
from stack_exchange_python_sdk.apis.paths.users_id_notifications import UsersIdNotifications
from stack_exchange_python_sdk.apis.paths.users_id_notifications_unread import UsersIdNotificationsUnread
from stack_exchange_python_sdk.apis.paths.users_id_privileges import UsersIdPrivileges
from stack_exchange_python_sdk.apis.paths.users_id_reputation_history_full import UsersIdReputationHistoryFull
from stack_exchange_python_sdk.apis.paths.users_id_tags_tags_top_answers import UsersIdTagsTagsTopAnswers
from stack_exchange_python_sdk.apis.paths.users_id_tags_tags_top_questions import UsersIdTagsTagsTopQuestions
from stack_exchange_python_sdk.apis.paths.users_id_top_answer_tags import UsersIdTopAnswerTags
from stack_exchange_python_sdk.apis.paths.users_id_top_question_tags import UsersIdTopQuestionTags
from stack_exchange_python_sdk.apis.paths.users_id_write_permissions import UsersIdWritePermissions

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCESSTOKENS_ACCESS_TOKENS: AccessTokensAccessTokens,
        PathValues.ACCESSTOKENS_ACCESS_TOKENS_INVALIDATE: AccessTokensAccessTokensInvalidate,
        PathValues.ANSWERS: Answers,
        PathValues.ANSWERS_IDS: AnswersIds,
        PathValues.ANSWERS_IDS_COMMENTS: AnswersIdsComments,
        PathValues.APPS_ACCESS_TOKENS_DEAUTHENTICATE: AppsAccessTokensDeAuthenticate,
        PathValues.BADGES: Badges,
        PathValues.BADGES_NAME: BadgesName,
        PathValues.BADGES_RECIPIENTS: BadgesRecipients,
        PathValues.BADGES_TAGS: BadgesTags,
        PathValues.BADGES_IDS: BadgesIds,
        PathValues.BADGES_IDS_RECIPIENTS: BadgesIdsRecipients,
        PathValues.COMMENTS: Comments,
        PathValues.COMMENTS_IDS: CommentsIds,
        PathValues.COMMENTS_ID_DELETE: CommentsIdDelete,
        PathValues.COMMENTS_ID_EDIT: CommentsIdEdit,
        PathValues.ERRORS: Errors,
        PathValues.ERRORS_ID: ErrorsId,
        PathValues.EVENTS: Events,
        PathValues.FILTERS_CREATE: FiltersCreate,
        PathValues.FILTERS_FILTERS: FiltersFilters,
        PathValues.INBOX: Inbox,
        PathValues.INBOX_UNREAD: InboxUnread,
        PathValues.INFO: Info,
        PathValues.ME: Me,
        PathValues.ME_ANSWERS: MeAnswers,
        PathValues.ME_ASSOCIATED: MeAssociated,
        PathValues.ME_BADGES: MeBadges,
        PathValues.ME_COMMENTS: MeComments,
        PathValues.ME_COMMENTS_TO_ID: MeCommentsToId,
        PathValues.ME_FAVORITES: MeFavorites,
        PathValues.ME_INBOX: MeInbox,
        PathValues.ME_INBOX_UNREAD: MeInboxUnread,
        PathValues.ME_MENTIONED: MeMentioned,
        PathValues.ME_MERGES: MeMerges,
        PathValues.ME_NOTIFICATIONS: MeNotifications,
        PathValues.ME_NOTIFICATIONS_UNREAD: MeNotificationsUnread,
        PathValues.ME_PRIVILEGES: MePrivileges,
        PathValues.ME_QUESTIONS: MeQuestions,
        PathValues.ME_QUESTIONS_FEATURED: MeQuestionsFeatured,
        PathValues.ME_QUESTIONS_NOANSWERS: MeQuestionsNoAnswers,
        PathValues.ME_QUESTIONS_UNACCEPTED: MeQuestionsUnaccepted,
        PathValues.ME_QUESTIONS_UNANSWERED: MeQuestionsUnanswered,
        PathValues.ME_REPUTATION: MeReputation,
        PathValues.ME_REPUTATIONHISTORY: MeReputationHistory,
        PathValues.ME_REPUTATIONHISTORY_FULL: MeReputationHistoryFull,
        PathValues.ME_SUGGESTEDEDITS: MeSuggestedEdits,
        PathValues.ME_TAGS: MeTags,
        PathValues.ME_TAGS_TAGS_TOPANSWERS: MeTagsTagsTopAnswers,
        PathValues.ME_TAGS_TAGS_TOPQUESTIONS: MeTagsTagsTopQuestions,
        PathValues.ME_TIMELINE: MeTimeline,
        PathValues.ME_TOPANSWERTAGS: MeTopAnswerTags,
        PathValues.ME_TOPQUESTIONTAGS: MeTopQuestionTags,
        PathValues.ME_WRITEPERMISSIONS: MeWritePermissions,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.NOTIFICATIONS_UNREAD: NotificationsUnread,
        PathValues.POSTS: Posts,
        PathValues.POSTS_IDS: PostsIds,
        PathValues.POSTS_IDS_COMMENTS: PostsIdsComments,
        PathValues.POSTS_IDS_REVISIONS: PostsIdsRevisions,
        PathValues.POSTS_IDS_SUGGESTEDEDITS: PostsIdsSuggestedEdits,
        PathValues.POSTS_ID_COMMENTS_ADD: PostsIdCommentsAdd,
        PathValues.PRIVILEGES: Privileges,
        PathValues.QUESTIONS: Questions,
        PathValues.QUESTIONS_FEATURED: QuestionsFeatured,
        PathValues.QUESTIONS_NOANSWERS: QuestionsNoAnswers,
        PathValues.QUESTIONS_UNANSWERED: QuestionsUnanswered,
        PathValues.QUESTIONS_IDS: QuestionsIds,
        PathValues.QUESTIONS_IDS_ANSWERS: QuestionsIdsAnswers,
        PathValues.QUESTIONS_IDS_COMMENTS: QuestionsIdsComments,
        PathValues.QUESTIONS_IDS_LINKED: QuestionsIdsLinked,
        PathValues.QUESTIONS_IDS_RELATED: QuestionsIdsRelated,
        PathValues.QUESTIONS_IDS_TIMELINE: QuestionsIdsTimeline,
        PathValues.REVISIONS_IDS: RevisionsIds,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_ADVANCED: SearchAdvanced,
        PathValues.SIMILAR: Similar,
        PathValues.SITES: Sites,
        PathValues.SUGGESTEDEDITS: SuggestedEdits,
        PathValues.SUGGESTEDEDITS_IDS: SuggestedEditsIds,
        PathValues.TAGS: Tags,
        PathValues.TAGS_MODERATORONLY: TagsModeratorOnly,
        PathValues.TAGS_REQUIRED: TagsRequired,
        PathValues.TAGS_SYNONYMS: TagsSynonyms,
        PathValues.TAGS_TAGS_FAQ: TagsTagsFaq,
        PathValues.TAGS_TAGS_INFO: TagsTagsInfo,
        PathValues.TAGS_TAGS_RELATED: TagsTagsRelated,
        PathValues.TAGS_TAGS_SYNONYMS: TagsTagsSynonyms,
        PathValues.TAGS_TAGS_WIKIS: TagsTagsWikis,
        PathValues.TAGS_TAG_TOPANSWERERS_PERIOD: TagsTagTopAnswerersPeriod,
        PathValues.TAGS_TAG_TOPASKERS_PERIOD: TagsTagTopAskersPeriod,
        PathValues.USERS: Users,
        PathValues.USERS_MODERATORS: UsersModerators,
        PathValues.USERS_MODERATORS_ELECTED: UsersModeratorsElected,
        PathValues.USERS_IDS: UsersIds,
        PathValues.USERS_IDS_ANSWERS: UsersIdsAnswers,
        PathValues.USERS_IDS_ASSOCIATED: UsersIdsAssociated,
        PathValues.USERS_IDS_BADGES: UsersIdsBadges,
        PathValues.USERS_IDS_COMMENTS: UsersIdsComments,
        PathValues.USERS_IDS_COMMENTS_TOID: UsersIdsCommentsToid,
        PathValues.USERS_IDS_FAVORITES: UsersIdsFavorites,
        PathValues.USERS_IDS_MENTIONED: UsersIdsMentioned,
        PathValues.USERS_IDS_MERGES: UsersIdsMerges,
        PathValues.USERS_IDS_QUESTIONS: UsersIdsQuestions,
        PathValues.USERS_IDS_QUESTIONS_FEATURED: UsersIdsQuestionsFeatured,
        PathValues.USERS_IDS_QUESTIONS_NOANSWERS: UsersIdsQuestionsNoAnswers,
        PathValues.USERS_IDS_QUESTIONS_UNACCEPTED: UsersIdsQuestionsUnaccepted,
        PathValues.USERS_IDS_QUESTIONS_UNANSWERED: UsersIdsQuestionsUnanswered,
        PathValues.USERS_IDS_REPUTATION: UsersIdsReputation,
        PathValues.USERS_IDS_REPUTATIONHISTORY: UsersIdsReputationHistory,
        PathValues.USERS_IDS_SUGGESTEDEDITS: UsersIdsSuggestedEdits,
        PathValues.USERS_IDS_TAGS: UsersIdsTags,
        PathValues.USERS_IDS_TIMELINE: UsersIdsTimeline,
        PathValues.USERS_ID_INBOX: UsersIdInbox,
        PathValues.USERS_ID_INBOX_UNREAD: UsersIdInboxUnread,
        PathValues.USERS_ID_NOTIFICATIONS: UsersIdNotifications,
        PathValues.USERS_ID_NOTIFICATIONS_UNREAD: UsersIdNotificationsUnread,
        PathValues.USERS_ID_PRIVILEGES: UsersIdPrivileges,
        PathValues.USERS_ID_REPUTATIONHISTORY_FULL: UsersIdReputationHistoryFull,
        PathValues.USERS_ID_TAGS_TAGS_TOPANSWERS: UsersIdTagsTagsTopAnswers,
        PathValues.USERS_ID_TAGS_TAGS_TOPQUESTIONS: UsersIdTagsTagsTopQuestions,
        PathValues.USERS_ID_TOPANSWERTAGS: UsersIdTopAnswerTags,
        PathValues.USERS_ID_TOPQUESTIONTAGS: UsersIdTopQuestionTags,
        PathValues.USERS_ID_WRITEPERMISSIONS: UsersIdWritePermissions,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCESSTOKENS_ACCESS_TOKENS: AccessTokensAccessTokens,
        PathValues.ACCESSTOKENS_ACCESS_TOKENS_INVALIDATE: AccessTokensAccessTokensInvalidate,
        PathValues.ANSWERS: Answers,
        PathValues.ANSWERS_IDS: AnswersIds,
        PathValues.ANSWERS_IDS_COMMENTS: AnswersIdsComments,
        PathValues.APPS_ACCESS_TOKENS_DEAUTHENTICATE: AppsAccessTokensDeAuthenticate,
        PathValues.BADGES: Badges,
        PathValues.BADGES_NAME: BadgesName,
        PathValues.BADGES_RECIPIENTS: BadgesRecipients,
        PathValues.BADGES_TAGS: BadgesTags,
        PathValues.BADGES_IDS: BadgesIds,
        PathValues.BADGES_IDS_RECIPIENTS: BadgesIdsRecipients,
        PathValues.COMMENTS: Comments,
        PathValues.COMMENTS_IDS: CommentsIds,
        PathValues.COMMENTS_ID_DELETE: CommentsIdDelete,
        PathValues.COMMENTS_ID_EDIT: CommentsIdEdit,
        PathValues.ERRORS: Errors,
        PathValues.ERRORS_ID: ErrorsId,
        PathValues.EVENTS: Events,
        PathValues.FILTERS_CREATE: FiltersCreate,
        PathValues.FILTERS_FILTERS: FiltersFilters,
        PathValues.INBOX: Inbox,
        PathValues.INBOX_UNREAD: InboxUnread,
        PathValues.INFO: Info,
        PathValues.ME: Me,
        PathValues.ME_ANSWERS: MeAnswers,
        PathValues.ME_ASSOCIATED: MeAssociated,
        PathValues.ME_BADGES: MeBadges,
        PathValues.ME_COMMENTS: MeComments,
        PathValues.ME_COMMENTS_TO_ID: MeCommentsToId,
        PathValues.ME_FAVORITES: MeFavorites,
        PathValues.ME_INBOX: MeInbox,
        PathValues.ME_INBOX_UNREAD: MeInboxUnread,
        PathValues.ME_MENTIONED: MeMentioned,
        PathValues.ME_MERGES: MeMerges,
        PathValues.ME_NOTIFICATIONS: MeNotifications,
        PathValues.ME_NOTIFICATIONS_UNREAD: MeNotificationsUnread,
        PathValues.ME_PRIVILEGES: MePrivileges,
        PathValues.ME_QUESTIONS: MeQuestions,
        PathValues.ME_QUESTIONS_FEATURED: MeQuestionsFeatured,
        PathValues.ME_QUESTIONS_NOANSWERS: MeQuestionsNoAnswers,
        PathValues.ME_QUESTIONS_UNACCEPTED: MeQuestionsUnaccepted,
        PathValues.ME_QUESTIONS_UNANSWERED: MeQuestionsUnanswered,
        PathValues.ME_REPUTATION: MeReputation,
        PathValues.ME_REPUTATIONHISTORY: MeReputationHistory,
        PathValues.ME_REPUTATIONHISTORY_FULL: MeReputationHistoryFull,
        PathValues.ME_SUGGESTEDEDITS: MeSuggestedEdits,
        PathValues.ME_TAGS: MeTags,
        PathValues.ME_TAGS_TAGS_TOPANSWERS: MeTagsTagsTopAnswers,
        PathValues.ME_TAGS_TAGS_TOPQUESTIONS: MeTagsTagsTopQuestions,
        PathValues.ME_TIMELINE: MeTimeline,
        PathValues.ME_TOPANSWERTAGS: MeTopAnswerTags,
        PathValues.ME_TOPQUESTIONTAGS: MeTopQuestionTags,
        PathValues.ME_WRITEPERMISSIONS: MeWritePermissions,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.NOTIFICATIONS_UNREAD: NotificationsUnread,
        PathValues.POSTS: Posts,
        PathValues.POSTS_IDS: PostsIds,
        PathValues.POSTS_IDS_COMMENTS: PostsIdsComments,
        PathValues.POSTS_IDS_REVISIONS: PostsIdsRevisions,
        PathValues.POSTS_IDS_SUGGESTEDEDITS: PostsIdsSuggestedEdits,
        PathValues.POSTS_ID_COMMENTS_ADD: PostsIdCommentsAdd,
        PathValues.PRIVILEGES: Privileges,
        PathValues.QUESTIONS: Questions,
        PathValues.QUESTIONS_FEATURED: QuestionsFeatured,
        PathValues.QUESTIONS_NOANSWERS: QuestionsNoAnswers,
        PathValues.QUESTIONS_UNANSWERED: QuestionsUnanswered,
        PathValues.QUESTIONS_IDS: QuestionsIds,
        PathValues.QUESTIONS_IDS_ANSWERS: QuestionsIdsAnswers,
        PathValues.QUESTIONS_IDS_COMMENTS: QuestionsIdsComments,
        PathValues.QUESTIONS_IDS_LINKED: QuestionsIdsLinked,
        PathValues.QUESTIONS_IDS_RELATED: QuestionsIdsRelated,
        PathValues.QUESTIONS_IDS_TIMELINE: QuestionsIdsTimeline,
        PathValues.REVISIONS_IDS: RevisionsIds,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_ADVANCED: SearchAdvanced,
        PathValues.SIMILAR: Similar,
        PathValues.SITES: Sites,
        PathValues.SUGGESTEDEDITS: SuggestedEdits,
        PathValues.SUGGESTEDEDITS_IDS: SuggestedEditsIds,
        PathValues.TAGS: Tags,
        PathValues.TAGS_MODERATORONLY: TagsModeratorOnly,
        PathValues.TAGS_REQUIRED: TagsRequired,
        PathValues.TAGS_SYNONYMS: TagsSynonyms,
        PathValues.TAGS_TAGS_FAQ: TagsTagsFaq,
        PathValues.TAGS_TAGS_INFO: TagsTagsInfo,
        PathValues.TAGS_TAGS_RELATED: TagsTagsRelated,
        PathValues.TAGS_TAGS_SYNONYMS: TagsTagsSynonyms,
        PathValues.TAGS_TAGS_WIKIS: TagsTagsWikis,
        PathValues.TAGS_TAG_TOPANSWERERS_PERIOD: TagsTagTopAnswerersPeriod,
        PathValues.TAGS_TAG_TOPASKERS_PERIOD: TagsTagTopAskersPeriod,
        PathValues.USERS: Users,
        PathValues.USERS_MODERATORS: UsersModerators,
        PathValues.USERS_MODERATORS_ELECTED: UsersModeratorsElected,
        PathValues.USERS_IDS: UsersIds,
        PathValues.USERS_IDS_ANSWERS: UsersIdsAnswers,
        PathValues.USERS_IDS_ASSOCIATED: UsersIdsAssociated,
        PathValues.USERS_IDS_BADGES: UsersIdsBadges,
        PathValues.USERS_IDS_COMMENTS: UsersIdsComments,
        PathValues.USERS_IDS_COMMENTS_TOID: UsersIdsCommentsToid,
        PathValues.USERS_IDS_FAVORITES: UsersIdsFavorites,
        PathValues.USERS_IDS_MENTIONED: UsersIdsMentioned,
        PathValues.USERS_IDS_MERGES: UsersIdsMerges,
        PathValues.USERS_IDS_QUESTIONS: UsersIdsQuestions,
        PathValues.USERS_IDS_QUESTIONS_FEATURED: UsersIdsQuestionsFeatured,
        PathValues.USERS_IDS_QUESTIONS_NOANSWERS: UsersIdsQuestionsNoAnswers,
        PathValues.USERS_IDS_QUESTIONS_UNACCEPTED: UsersIdsQuestionsUnaccepted,
        PathValues.USERS_IDS_QUESTIONS_UNANSWERED: UsersIdsQuestionsUnanswered,
        PathValues.USERS_IDS_REPUTATION: UsersIdsReputation,
        PathValues.USERS_IDS_REPUTATIONHISTORY: UsersIdsReputationHistory,
        PathValues.USERS_IDS_SUGGESTEDEDITS: UsersIdsSuggestedEdits,
        PathValues.USERS_IDS_TAGS: UsersIdsTags,
        PathValues.USERS_IDS_TIMELINE: UsersIdsTimeline,
        PathValues.USERS_ID_INBOX: UsersIdInbox,
        PathValues.USERS_ID_INBOX_UNREAD: UsersIdInboxUnread,
        PathValues.USERS_ID_NOTIFICATIONS: UsersIdNotifications,
        PathValues.USERS_ID_NOTIFICATIONS_UNREAD: UsersIdNotificationsUnread,
        PathValues.USERS_ID_PRIVILEGES: UsersIdPrivileges,
        PathValues.USERS_ID_REPUTATIONHISTORY_FULL: UsersIdReputationHistoryFull,
        PathValues.USERS_ID_TAGS_TAGS_TOPANSWERS: UsersIdTagsTagsTopAnswers,
        PathValues.USERS_ID_TAGS_TAGS_TOPQUESTIONS: UsersIdTagsTagsTopQuestions,
        PathValues.USERS_ID_TOPANSWERTAGS: UsersIdTopAnswerTags,
        PathValues.USERS_ID_TOPQUESTIONTAGS: UsersIdTopQuestionTags,
        PathValues.USERS_ID_WRITEPERMISSIONS: UsersIdWritePermissions,
    }
)
