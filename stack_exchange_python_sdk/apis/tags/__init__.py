# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from stack_exchange_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    USER = "User"
    ANSWER = "Answer"
    TAG = "Tag"
    QUESTION = "Question"
    BADGE = "Badge"
    COMMENT = "Comment"
    POST = "Post"
    NOTIFICATION = "Notification"
    ACCESS_TOKEN = "AccessToken"
    MESSAGE = "Message"
    REPUTATION = "Reputation"
    EDIT = "Edit"
    ERROR = "Error"
    FILTER = "Filter"
    INFORMATION = "Information"
    PRIVILEGE = "Privilege"
    QUERY = "Query"
    EVENT = "Event"
    ASSOCIATED = "Associated"
    FAVORITE = "Favorite"
    MENTION = "Mention"
    MERGE = "Merge"
    TIMELINE = "Timeline"
    PERMISSION = "Permission"
    REVISION = "Revision"
    SEARCH = "Search"
    SITE = "Site"
