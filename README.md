<div align="left">

[![Visit Stack exchange](./header.png)](https://api.stackexchange.com)

# Stack exchange<a id="stack-exchange"></a>

Stack Exchange is a network of 130+ Q&A communities including Stack Overflow.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`stackexchange.access_token.deauthenticate_list`](#stackexchangeaccess_tokendeauthenticate_list)
  * [`stackexchange.access_token.invalidate_list`](#stackexchangeaccess_tokeninvalidate_list)
  * [`stackexchange.access_token.list_properties_for_multiple_tokens`](#stackexchangeaccess_tokenlist_properties_for_multiple_tokens)
  * [`stackexchange.answer.get_comments_by_ids`](#stackexchangeanswerget_comments_by_ids)
  * [`stackexchange.answer.get_list`](#stackexchangeanswerget_list)
  * [`stackexchange.answer.get_list_by_ids`](#stackexchangeanswerget_list_by_ids)
  * [`stackexchange.answer.get_list_by_question_ids`](#stackexchangeanswerget_list_by_question_ids)
  * [`stackexchange.answer.get_list_of_unanswered_questions`](#stackexchangeanswerget_list_of_unanswered_questions)
  * [`stackexchange.answer.get_user_answers_list`](#stackexchangeanswerget_user_answers_list)
  * [`stackexchange.answer.get_user_top_answers`](#stackexchangeanswerget_user_top_answers)
  * [`stackexchange.answer.get_user_top_tags`](#stackexchangeanswerget_user_top_tags)
  * [`stackexchange.answer.list_no_answer_questions`](#stackexchangeanswerlist_no_answer_questions)
  * [`stackexchange.answer.list_no_answer_questions_0`](#stackexchangeanswerlist_no_answer_questions_0)
  * [`stackexchange.answer.tag_top_answerers`](#stackexchangeanswertag_top_answerers)
  * [`stackexchange.answer.user_unanswered_questions_get`](#stackexchangeansweruser_unanswered_questions_get)
  * [`stackexchange.associated.get_user_accounts`](#stackexchangeassociatedget_user_accounts)
  * [`stackexchange.badge.get_all_named_badges`](#stackexchangebadgeget_all_named_badges)
  * [`stackexchange.badge.get_badges_by_ids`](#stackexchangebadgeget_badges_by_ids)
  * [`stackexchange.badge.get_recent_awarded_badges`](#stackexchangebadgeget_recent_awarded_badges)
  * [`stackexchange.badge.get_recent_awarded_recipients`](#stackexchangebadgeget_recent_awarded_recipients)
  * [`stackexchange.badge.get_user_badges`](#stackexchangebadgeget_user_badges)
  * [`stackexchange.badge.list_badges`](#stackexchangebadgelist_badges)
  * [`stackexchange.badge.list_tags_badges`](#stackexchangebadgelist_tags_badges)
  * [`stackexchange.comment.delete_action`](#stackexchangecommentdelete_action)
  * [`stackexchange.comment.edit_existing`](#stackexchangecommentedit_existing)
  * [`stackexchange.comment.get_comments_by_ids`](#stackexchangecommentget_comments_by_ids)
  * [`stackexchange.comment.get_comments_list`](#stackexchangecommentget_comments_list)
  * [`stackexchange.comment.get_reply_list`](#stackexchangecommentget_reply_list)
  * [`stackexchange.comment.list_comments`](#stackexchangecommentlist_comments)
  * [`stackexchange.comment.list_owned_comments`](#stackexchangecommentlist_owned_comments)
  * [`stackexchange.edit.get_user_suggested_edits`](#stackexchangeeditget_user_suggested_edits)
  * [`stackexchange.edit.list_suggested_edits`](#stackexchangeeditlist_suggested_edits)
  * [`stackexchange.edit.list_suggested_edits_0`](#stackexchangeeditlist_suggested_edits_0)
  * [`stackexchange.error.generate_error`](#stackexchangeerrorgenerate_error)
  * [`stackexchange.error.list_errors`](#stackexchangeerrorlist_errors)
  * [`stackexchange.event.list_events`](#stackexchangeeventlist_events)
  * [`stackexchange.favorite.get_user_favorites`](#stackexchangefavoriteget_user_favorites)
  * [`stackexchange.filter.create_filter`](#stackexchangefiltercreate_filter)
  * [`stackexchange.filter.get_filter_details_by_ids`](#stackexchangefilterget_filter_details_by_ids)
  * [`stackexchange.information.get_statistics`](#stackexchangeinformationget_statistics)
  * [`stackexchange.information.get_tags_list`](#stackexchangeinformationget_tags_list)
  * [`stackexchange.mention.user_comments_list`](#stackexchangementionuser_comments_list)
  * [`stackexchange.merge.get_account_merge_list`](#stackexchangemergeget_account_merge_list)
  * [`stackexchange.message.get_inbox_items`](#stackexchangemessageget_inbox_items)
  * [`stackexchange.message.get_unread_items`](#stackexchangemessageget_unread_items)
  * [`stackexchange.message.list_inbox_items`](#stackexchangemessagelist_inbox_items)
  * [`stackexchange.notification.get_unread_items_in_inbox`](#stackexchangenotificationget_unread_items_in_inbox)
  * [`stackexchange.notification.get_unread_items_in_inbox_0`](#stackexchangenotificationget_unread_items_in_inbox_0)
  * [`stackexchange.notification.get_user_notifications`](#stackexchangenotificationget_user_notifications)
  * [`stackexchange.notification.get_user_notifications_list`](#stackexchangenotificationget_user_notifications_list)
  * [`stackexchange.notification.get_user_unread_notifications`](#stackexchangenotificationget_user_unread_notifications)
  * [`stackexchange.permission.get_user_write_permissions`](#stackexchangepermissionget_user_write_permissions)
  * [`stackexchange.post.add_comment`](#stackexchangepostadd_comment)
  * [`stackexchange.post.comments_by_ids_get`](#stackexchangepostcomments_by_ids_get)
  * [`stackexchange.post.get_all_posts`](#stackexchangepostget_all_posts)
  * [`stackexchange.post.get_post_revisions_by_ids`](#stackexchangepostget_post_revisions_by_ids)
  * [`stackexchange.post.get_posts_by_ids`](#stackexchangepostget_posts_by_ids)
  * [`stackexchange.post.list_suggested_edits`](#stackexchangepostlist_suggested_edits)
  * [`stackexchange.privilege.get_earnable_list`](#stackexchangeprivilegeget_earnable_list)
  * [`stackexchange.privilege.get_user_privileges`](#stackexchangeprivilegeget_user_privileges)
  * [`stackexchange.query.similar_questions_search`](#stackexchangequerysimilar_questions_search)
  * [`stackexchange.query.site_questions_search`](#stackexchangequerysite_questions_search)
  * [`stackexchange.question.get_all_questions`](#stackexchangequestionget_all_questions)
  * [`stackexchange.question.get_by_ids`](#stackexchangequestionget_by_ids)
  * [`stackexchange.question.get_linked_questions`](#stackexchangequestionget_linked_questions)
  * [`stackexchange.question.get_timeline_events`](#stackexchangequestionget_timeline_events)
  * [`stackexchange.question.get_unaccepted_list`](#stackexchangequestionget_unaccepted_list)
  * [`stackexchange.question.get_user_featured`](#stackexchangequestionget_user_featured)
  * [`stackexchange.question.get_user_questions_list`](#stackexchangequestionget_user_questions_list)
  * [`stackexchange.question.list_featured_questions`](#stackexchangequestionlist_featured_questions)
  * [`stackexchange.question.list_related_questions`](#stackexchangequestionlist_related_questions)
  * [`stackexchange.reputation.get_full_history`](#stackexchangereputationget_full_history)
  * [`stackexchange.reputation.get_user_reputation_changes`](#stackexchangereputationget_user_reputation_changes)
  * [`stackexchange.reputation.get_user_reputation_history`](#stackexchangereputationget_user_reputation_history)
  * [`stackexchange.revision.list_revisions_by_ids`](#stackexchangerevisionlist_revisions_by_ids)
  * [`stackexchange.search.site_questions_advanced_search`](#stackexchangesearchsite_questions_advanced_search)
  * [`stackexchange.site.list_sites`](#stackexchangesitelist_sites)
  * [`stackexchange.tag.get_faq_questions`](#stackexchangetagget_faq_questions)
  * [`stackexchange.tag.get_moderator_only_tags_list`](#stackexchangetagget_moderator_only_tags_list)
  * [`stackexchange.tag.get_related_tags`](#stackexchangetagget_related_tags)
  * [`stackexchange.tag.get_tag_info`](#stackexchangetagget_tag_info)
  * [`stackexchange.tag.get_tag_wikis`](#stackexchangetagget_tag_wikis)
  * [`stackexchange.tag.get_top_askers_by_period`](#stackexchangetagget_top_askers_by_period)
  * [`stackexchange.tag.get_user_tags_list`](#stackexchangetagget_user_tags_list)
  * [`stackexchange.tag.get_user_top_questions`](#stackexchangetagget_user_top_questions)
  * [`stackexchange.tag.get_user_top_tags_list`](#stackexchangetagget_user_top_tags_list)
  * [`stackexchange.tag.list_required_tags`](#stackexchangetaglist_required_tags)
  * [`stackexchange.tag.list_synonyms`](#stackexchangetaglist_synonyms)
  * [`stackexchange.tag.synonyms_list`](#stackexchangetagsynonyms_list)
  * [`stackexchange.timeline.get_user_timeline`](#stackexchangetimelineget_user_timeline)
  * [`stackexchange.user.get_associated_accounts`](#stackexchangeuserget_associated_accounts)
  * [`stackexchange.user.get_comments_by_ids`](#stackexchangeuserget_comments_by_ids)
  * [`stackexchange.user.get_favorites_list`](#stackexchangeuserget_favorites_list)
  * [`stackexchange.user.get_featured_questions`](#stackexchangeuserget_featured_questions)
  * [`stackexchange.user.get_full_reputation_history`](#stackexchangeuserget_full_reputation_history)
  * [`stackexchange.user.get_inbox_items`](#stackexchangeuserget_inbox_items)
  * [`stackexchange.user.get_inbox_unread`](#stackexchangeuserget_inbox_unread)
  * [`stackexchange.user.get_notifications_list`](#stackexchangeuserget_notifications_list)
  * [`stackexchange.user.get_privileges_list`](#stackexchangeuserget_privileges_list)
  * [`stackexchange.user.get_questions_by_user_ids`](#stackexchangeuserget_questions_by_user_ids)
  * [`stackexchange.user.get_reputation_changes`](#stackexchangeuserget_reputation_changes)
  * [`stackexchange.user.get_reputation_history`](#stackexchangeuserget_reputation_history)
  * [`stackexchange.user.get_suggested_edits_by_ids`](#stackexchangeuserget_suggested_edits_by_ids)
  * [`stackexchange.user.get_tags`](#stackexchangeuserget_tags)
  * [`stackexchange.user.get_top_question_tags`](#stackexchangeuserget_top_question_tags)
  * [`stackexchange.user.get_top_questions_by_tags`](#stackexchangeuserget_top_questions_by_tags)
  * [`stackexchange.user.get_unaccepted_questions`](#stackexchangeuserget_unaccepted_questions)
  * [`stackexchange.user.get_unanswered_questions`](#stackexchangeuserget_unanswered_questions)
  * [`stackexchange.user.get_unread_notifications`](#stackexchangeuserget_unread_notifications)
  * [`stackexchange.user.get_user`](#stackexchangeuserget_user)
  * [`stackexchange.user.get_user_answers_list`](#stackexchangeuserget_user_answers_list)
  * [`stackexchange.user.get_user_comments_by_ids_and_toid`](#stackexchangeuserget_user_comments_by_ids_and_toid)
  * [`stackexchange.user.get_user_profiles_by_ids`](#stackexchangeuserget_user_profiles_by_ids)
  * [`stackexchange.user.get_user_timeline_by_ids`](#stackexchangeuserget_user_timeline_by_ids)
  * [`stackexchange.user.get_user_top_answer_tags`](#stackexchangeuserget_user_top_answer_tags)
  * [`stackexchange.user.get_user_top_answers`](#stackexchangeuserget_user_top_answers)
  * [`stackexchange.user.get_write_permissions`](#stackexchangeuserget_write_permissions)
  * [`stackexchange.user.list_account_merges`](#stackexchangeuserlist_account_merges)
  * [`stackexchange.user.list_elected_moderator_users`](#stackexchangeuserlist_elected_moderator_users)
  * [`stackexchange.user.list_moderator_users`](#stackexchangeuserlist_moderator_users)
  * [`stackexchange.user.list_no_answer_questions`](#stackexchangeuserlist_no_answer_questions)
  * [`stackexchange.user.list_user_badges`](#stackexchangeuserlist_user_badges)
  * [`stackexchange.user.list_users`](#stackexchangeuserlist_users)
  * [`stackexchange.user.mentioned_comments_list`](#stackexchangeusermentioned_comments_list)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Stack%20Exchange&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from stack_exchange_python_sdk import StackExchange, ApiException

stackexchange = StackExchange()

try:
    deauthenticate_list_response = stackexchange.access_token.deauthenticate_list(
        access_tokens="accessTokens_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
    print(deauthenticate_list_response)
except ApiException as e:
    print("Exception when calling AccessTokenApi.deauthenticate_list: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from stack_exchange_python_sdk import StackExchange, ApiException

stackexchange = StackExchange()


async def main():
    try:
        deauthenticate_list_response = (
            await stackexchange.access_token.adeauthenticate_list(
                access_tokens="accessTokens_example",
                pagesize=1,
                page=1,
                filter="string_example",
                param_callback="string_example",
            )
        )
        print(deauthenticate_list_response)
    except ApiException as e:
        print("Exception when calling AccessTokenApi.deauthenticate_list: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from stack_exchange_python_sdk import StackExchange, ApiException

stackexchange = StackExchange()

try:
    deauthenticate_list_response = stackexchange.access_token.raw.deauthenticate_list(
        access_tokens="accessTokens_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
    pprint(deauthenticate_list_response.body)
    pprint(deauthenticate_list_response.headers)
    pprint(deauthenticate_list_response.status)
    pprint(deauthenticate_list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccessTokenApi.deauthenticate_list: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `stackexchange.access_token.deauthenticate_list`<a id="stackexchangeaccess_tokendeauthenticate_list"></a>

Passing valid access_tokens to this method causes the application that created them to be de-authorized by the user associated with each access_token. This will remove the application from their apps tab, and cause all other existing access_tokens to be destroyed.
 
This method is meant for uninstalling applications, recovering from access_token leaks, or simply as a stronger form of /access-tokens/{accessTokens}/invalidate.
 
Nothing prevents a user from re-authenticate to an application that has de-authenticated itself, the user will be prompted to approve the application again however.
 
{accessTokens} can contain up to 20 access tokens. These are obtained by authenticating a user using OAuth 2.0.
 
This method returns a list of access_tokens.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deauthenticate_list_response = stackexchange.access_token.deauthenticate_list(
    access_tokens="accessTokens_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access_tokens: `str`<a id="access_tokens-str"></a>

String list (semicolon delimited).

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokens`](./stack_exchange_python_sdk/pydantic/access_tokens.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/apps/{accessTokens}/de-authenticate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.access_token.invalidate_list`<a id="stackexchangeaccess_tokeninvalidate_list"></a>

Immediately expires the access tokens passed. This method is meant to allow an application to discard any active access tokens it no longer needs.
 
{accessTokens} can contain up to 20 access tokens. These are obtained by authenticating a user using OAuth 2.0.
 
This method returns a list of access_tokens.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invalidate_list_response = stackexchange.access_token.invalidate_list(
    access_tokens="accessTokens_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access_tokens: `str`<a id="access_tokens-str"></a>

String list (semicolon delimited).

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokens`](./stack_exchange_python_sdk/pydantic/access_tokens.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access-tokens/{accessTokens}/invalidate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.access_token.list_properties_for_multiple_tokens`<a id="stackexchangeaccess_tokenlist_properties_for_multiple_tokens"></a>

Reads the properties for a set of access tokens.
 
{accessTokens} can contain up to 20 access tokens. These are obtained by authenticating a user using OAuth 2.0.
 
This method returns a list of access_tokens.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_properties_for_multiple_tokens_response = (
    stackexchange.access_token.list_properties_for_multiple_tokens(
        access_tokens="accessTokens_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access_tokens: `str`<a id="access_tokens-str"></a>

String list (semicolon delimited).

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokens`](./stack_exchange_python_sdk/pydantic/access_tokens.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access-tokens/{accessTokens}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_comments_by_ids`<a id="stackexchangeanswerget_comments_by_ids"></a>

Gets the comments on a set of answers.
 
If you know that you have an answer id and need the comments, use this method. If you know you have a question id, use /questions/{id}/comments. If you are unsure, use /posts/{id}/comments.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for answer_id on answer objects.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comments_by_ids_response = stackexchange.answer.get_comments_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/answers/{ids}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_list`<a id="stackexchangeanswerget_list"></a>

Returns all the undeleted answers in the system.
 
The sorts accepted by this method operate on the follow fields of the answer object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of answers.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = stackexchange.answer.get_list(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Answers`](./stack_exchange_python_sdk/pydantic/answers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_list_by_ids`<a id="stackexchangeanswerget_list_by_ids"></a>

Gets the set of answers identified by ids.
 
This is meant for batch fetcing of questions. A useful trick to poll for updates is to sort by activity, with a minimum date of the last time you polled.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for answer_id on answer objects.
 
The sorts accepted by this method operate on the follow fields of the answer object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of answers.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_by_ids_response = stackexchange.answer.get_list_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Answers`](./stack_exchange_python_sdk/pydantic/answers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/answers/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_list_by_question_ids`<a id="stackexchangeanswerget_list_by_question_ids"></a>

Gets the answers to a set of questions identified in id.
 
This method is most useful if you have a set of interesting questions, and you wish to obtain all of their answers at once or if you are polling for new or updates answers (in conjunction with sort=activity).
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for question_id on question objects.
 
The sorts accepted by this method operate on the follow fields of the answer object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of answers.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_by_question_ids_response = stackexchange.answer.get_list_by_question_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Answers`](./stack_exchange_python_sdk/pydantic/answers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/{ids}/answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_list_of_unanswered_questions`<a id="stackexchangeanswerget_list_of_unanswered_questions"></a>

Returns questions the site considers to be unanswered.
 
Note that just because a question has an answer, that does not mean it is considered answered. While the rules are subject to change, at this time a question must have at least one upvoted answer to be considered answered.
 
To constrain questions returned to those with a set of tags, use the tagged parameter with a semi-colon delimited list of tags. This is an and contraint, passing tagged=c;java will return only those questions with both tags. As such, passing more than 5 tags will always return zero results.
 
Compare with /questions/no-answers.
 
This method corresponds roughly with the unanswered tab.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_of_unanswered_questions_response = (
    stackexchange.answer.get_list_of_unanswered_questions(
        site="site_example",
        tagged="string_example",
        order="desc",
        max="string_example",
        min="string_example",
        sort="activity",
        fromdate=1,
        todate=1,
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### tagged: `str`<a id="tagged-str"></a>

String list (semicolon delimited).

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/unanswered` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_user_answers_list`<a id="stackexchangeanswerget_user_answers_list"></a>

Returns the answers owned by the user associated with the given access_token.
 
This method returns a list of answers.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_answers_list_response = stackexchange.answer.get_user_answers_list(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Answers`](./stack_exchange_python_sdk/pydantic/answers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_user_top_answers`<a id="stackexchangeanswerget_user_top_answers"></a>

Returns the top 30 answers the user associated with the given access_token has posted in response to questions with the given tags.
 
This method returns a list of answers.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_top_answers_response = stackexchange.answer.get_user_top_answers(
    tags="tags_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Answers`](./stack_exchange_python_sdk/pydantic/answers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tags/{tags}/top-answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.get_user_top_tags`<a id="stackexchangeanswerget_user_top_tags"></a>

Returns the user identified by access_token's top 30 tags by answer score.
 
This method returns a list of top tag objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_top_tags_response = stackexchange.answer.get_user_top_tags(
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TopTagObjects`](./stack_exchange_python_sdk/pydantic/top_tag_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/top-answer-tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.list_no_answer_questions`<a id="stackexchangeanswerlist_no_answer_questions"></a>

Returns the questions owned by the user associated with the given access_token that have no answers.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_no_answer_questions_response = stackexchange.answer.list_no_answer_questions(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/questions/no-answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.list_no_answer_questions_0`<a id="stackexchangeanswerlist_no_answer_questions_0"></a>

Returns questions which have received no answers.
 
Compare with /questions/unanswered which mearly returns questions that the sites consider insufficiently well answered.
 
This method corresponds roughly with the this site tab.
 
To constrain questions returned to those with a set of tags, use the tagged parameter with a semi-colon delimited list of tags. This is an and contraint, passing tagged=c;java will return only those questions with both tags. As such, passing more than 5 tags will always return zero results.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_no_answer_questions_0_response = stackexchange.answer.list_no_answer_questions_0(
    site="site_example",
    tagged="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### tagged: `str`<a id="tagged-str"></a>

String list (semicolon delimited).

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/no-answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.tag_top_answerers`<a id="stackexchangeanswertag_top_answerers"></a>

Returns the top 30 answerers active in a single tag, of either all-time or the last 30 days.
 
This is a view onto the data presented on the tag info page on the sites.
 
This method returns a list of tag score objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tag_top_answerers_response = stackexchange.answer.tag_top_answerers(
    tag="tag_example",
    period="all_time",
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag: `str`<a id="tag-str"></a>

##### period: `str`<a id="period-str"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TagScoreObjects`](./stack_exchange_python_sdk/pydantic/tag_score_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag}/top-answerers/{period}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.answer.user_unanswered_questions_get`<a id="stackexchangeansweruser_unanswered_questions_get"></a>

Returns the questions owned by the user associated with the given access_token that are not considered answered.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
user_unanswered_questions_get_response = (
    stackexchange.answer.user_unanswered_questions_get(
        site="site_example",
        order="desc",
        max="string_example",
        min="string_example",
        sort="activity",
        fromdate=1,
        todate=1,
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/questions/unanswered` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.associated.get_user_accounts`<a id="stackexchangeassociatedget_user_accounts"></a>

Returns all of a user's associated accounts, given an access_token for them.
 
This method returns a list of network users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_accounts_response = stackexchange.associated.get_user_accounts(
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkUsers`](./stack_exchange_python_sdk/pydantic/network_users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/associated` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.badge.get_all_named_badges`<a id="stackexchangebadgeget_all_named_badges"></a>

Gets all explicitly named badges in the system.
 
A named badged stands in opposition to a tag-based badge. These are referred to as general badges on the sites themselves.
 
For the rank sort, bronze is greater than silver which is greater than gold. Along with sort=rank, set max=gold for just gold badges, max=silver&min=silver for just silver, and min=bronze for just bronze.
 
rank is the default sort.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_named_badges_response = stackexchange.badge.get_all_named_badges(
    site="site_example",
    inname="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="rank",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### inname: `str`<a id="inname-str"></a>

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = rank => string sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = rank => string sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/badges/name` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.badge.get_badges_by_ids`<a id="stackexchangebadgeget_badges_by_ids"></a>

Gets the badges identified in id.
 
Note that badge ids are not constant across sites, and thus should be looked up via the /badges method. A badge id on a single site is, however, guaranteed to be stable.
 
Badge sorts are a tad complicated. For the purposes of sorting (and min/max) tag_based is considered to be greater than named.
 
This means that you can get a list of all tag based badges by passing min=tag_based, and conversely all the named badges by passing max=named, with sort=type.
 
For ranks, bronze is greater than silver which is greater than gold. Along with sort=rank, set max=gold for just gold badges, max=silver&min=silver for just silver, and min=bronze for just bronze.
 
rank is the default sort.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for badge_id on badge objects.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_badges_by_ids_response = stackexchange.badge.get_badges_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="rank",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = rank => string sort = name => string sort = type => string 

##### min: `str`<a id="min-str"></a>

sort = rank => string sort = name => string sort = type => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/badges/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.badge.get_recent_awarded_badges`<a id="stackexchangebadgeget_recent_awarded_badges"></a>

Returns recently awarded badges in the system.
 
As these badges have been awarded, they will have the badge.user property set.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_awarded_badges_response = stackexchange.badge.get_recent_awarded_badges(
    site="site_example",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/badges/recipients` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.badge.get_recent_awarded_recipients`<a id="stackexchangebadgeget_recent_awarded_recipients"></a>

Returns recently awarded badges in the system, constrained to a certain set of badges.
 
As these badges have been awarded, they will have the badge.user property set.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for badge_id on badge objects.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_awarded_recipients_response = (
    stackexchange.badge.get_recent_awarded_recipients(
        ids="ids_example",
        site="site_example",
        fromdate=1,
        todate=1,
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/badges/{ids}/recipients` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.badge.get_user_badges`<a id="stackexchangebadgeget_user_badges"></a>

Returns the badges earned by the user associated with the given access_token.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_badges_response = stackexchange.badge.get_user_badges(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="rank",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = rank => string sort = name => string sort = type => string 

##### min: `str`<a id="min-str"></a>

sort = rank => string sort = name => string sort = type => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/badges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.badge.list_badges`<a id="stackexchangebadgelist_badges"></a>

Returns all the badges in the system.
 
Badge sorts are a tad complicated. For the purposes of sorting (and min/max) tag_based is considered to be greater than named.
 
This means that you can get a list of all tag based badges by passing min=tag_based, and conversely all the named badges by passing max=named, with sort=type.
 
For ranks, bronze is greater than silver which is greater than gold. Along with sort=rank, set max=gold for just gold badges, max=silver&min=silver for just silver, and min=bronze for just bronze.
 
rank is the default sort.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_badges_response = stackexchange.badge.list_badges(
    site="site_example",
    inname="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="rank",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### inname: `str`<a id="inname-str"></a>

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = rank => string sort = name => string sort = type => string 

##### min: `str`<a id="min-str"></a>

sort = rank => string sort = name => string sort = type => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/badges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.badge.list_tags_badges`<a id="stackexchangebadgelist_tags_badges"></a>

Returns the badges that are awarded for participation in specific tags.
 
For the rank sort, bronze is greater than silver which is greater than gold. Along with sort=rank, set max=gold for just gold badges, max=silver&min=silver for just silver, and min=bronze for just bronze.
 
rank is the default sort.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tags_badges_response = stackexchange.badge.list_tags_badges(
    site="site_example",
    inname="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="rank",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### inname: `str`<a id="inname-str"></a>

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = rank => string sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = rank => string sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/badges/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.comment.delete_action`<a id="stackexchangecommentdelete_action"></a>

Deletes a comment.
 
Use an access_token with write_access to delete a comment.
 
In practice, this method will never return an object.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
stackexchange.comment.delete_action(
    id=1,
    site="site_example",
    filter="string_example",
    param_callback="string_example",
    preview=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### preview: `bool`<a id="preview-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{id}/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.comment.edit_existing`<a id="stackexchangecommentedit_existing"></a>

Edit an existing comment.
 
Use an access_token with write_access to edit an existing comment.
 
This method return the created comment.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_existing_response = stackexchange.comment.edit_existing(
    id=1,
    site="site_example",
    filter="string_example",
    param_callback="string_example",
    body="string_example",
    preview=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### body: `str`<a id="body-str"></a>

##### preview: `bool`<a id="preview-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CreatedComment`](./stack_exchange_python_sdk/pydantic/created_comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{id}/edit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.comment.get_comments_by_ids`<a id="stackexchangecommentget_comments_by_ids"></a>

Gets the comments identified in id.
 
This method is most useful if you have a cache of comment ids obtained through other means (such as /questions/{id}/comments) but suspect the data may be stale.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for comment_id on comment objects.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comments_by_ids_response = stackexchange.comment.get_comments_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.comment.get_comments_list`<a id="stackexchangecommentget_comments_list"></a>

Gets the comments on a question.
 
If you know that you have an question id and need the comments, use this method. If you know you have a answer id, use /answers/{ids}/comments. If you are unsure, use /posts/{ids}/comments.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for question_id on question objects.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comments_list_response = stackexchange.comment.get_comments_list(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/{ids}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.comment.get_reply_list`<a id="stackexchangecommentget_reply_list"></a>

Returns the comments owned by the user associated with the given access_token that are in reply to the user identified by {toId}.
 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_reply_list_response = stackexchange.comment.get_reply_list(
    to_id=1,
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### to_id: `int`<a id="to_id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/comments/{toId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.comment.list_comments`<a id="stackexchangecommentlist_comments"></a>

Gets all the comments on the site.
 
If you're filtering for interesting comments (by score, creation date, etc.) make use of the sort paramter with appropriate min and max values.
 
If you're looking to query conversations between users, instead use the /users/{ids}/mentioned and /users/{ids}/comments/{toid} methods.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_comments_response = stackexchange.comment.list_comments(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.comment.list_owned_comments`<a id="stackexchangecommentlist_owned_comments"></a>

Returns the comments owned by the user associated with the given access_token.
 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_owned_comments_response = stackexchange.comment.list_owned_comments(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.edit.get_user_suggested_edits`<a id="stackexchangeeditget_user_suggested_edits"></a>

Returns the suggested edits the user identified by access_token has submitted.
 
This method returns a list of suggested-edits.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_suggested_edits_response = stackexchange.edit.get_user_suggested_edits(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`SuggestedEdits`](./stack_exchange_python_sdk/pydantic/suggested_edits.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/suggested-edits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.edit.list_suggested_edits`<a id="stackexchangeeditlist_suggested_edits"></a>

Returns all the suggested edits in the systems.
 
This method returns a list of suggested-edits.
 
The sorts accepted by this method operate on the follow fields of the suggested_edit object:
 - creation - creation_date
 - approval - approval_date Does not return unapproved suggested_edits
 - rejection - rejection_date Does not return unrejected suggested_edits
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_suggested_edits_response = stackexchange.edit.list_suggested_edits(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`SuggestedEdits`](./stack_exchange_python_sdk/pydantic/suggested_edits.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/suggested-edits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.edit.list_suggested_edits_0`<a id="stackexchangeeditlist_suggested_edits_0"></a>

Returns suggested edits identified in ids.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for suggested_edit_id on suggested_edit objects.
 
The sorts accepted by this method operate on the follow fields of the suggested_edit object:
 - creation - creation_date
 - approval - approval_date Does not return unapproved suggested_edits
 - rejection - rejection_date Does not return unrejected suggested_edits
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of suggested-edits.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_suggested_edits_0_response = stackexchange.edit.list_suggested_edits_0(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`SuggestedEdits`](./stack_exchange_python_sdk/pydantic/suggested_edits.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/suggested-edits/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.error.generate_error`<a id="stackexchangeerrorgenerate_error"></a>

This method allows you to generate an error.
 
This method is only intended for use when testing an application or library. Unlike other methods in the API, its contract is not frozen, and new error codes may be added at any time.
 
This method results in an error, which will be expressed with a 400 HTTP status code and setting the error* properties on the wrapper object.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_error_response = stackexchange.error.generate_error(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Error`](./stack_exchange_python_sdk/pydantic/error.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/errors/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.error.list_errors`<a id="stackexchangeerrorlist_errors"></a>

Returns the various error codes that can be produced by the API.
 
This method is provided for discovery, documentation, and testing purposes, it is not expected many applications will consume it during normal operation.
 
For testing purposes, look into the /errors/{id} method which simulates errors given a code.
 
This method returns a list of errors.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_errors_response = stackexchange.error.list_errors(
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Errors`](./stack_exchange_python_sdk/pydantic/errors.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/errors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.event.list_events`<a id="stackexchangeeventlist_events"></a>

Returns a stream of events that have occurred on the site.
 
The API considers the following "events":
 - posting a question
 - posting an answer
 - posting a comment
 - editing a post
 - creating a user


  


 
Events are only accessible for 15 minutes after they occurred, and by default only events in the last 5 minutes are returned. You can specify the age of the oldest event returned by setting the since parameter.
 
It is advised that developers batch events by ids and make as few subsequent requests to other methods as possible.
 
This method returns a list of events.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_events_response = stackexchange.event.list_events(
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
    since=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### since: `int`<a id="since-int"></a>

Unix date.

#### 🔄 Return<a id="🔄-return"></a>

[`Events`](./stack_exchange_python_sdk/pydantic/events.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.favorite.get_user_favorites`<a id="stackexchangefavoriteget_user_favorites"></a>

Returns the questions favorites by the user associated with the given access_token.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_favorites_response = stackexchange.favorite.get_user_favorites(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = added => date 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = added => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/favorites` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.filter.create_filter`<a id="stackexchangefiltercreate_filter"></a>

Creates a new filter given a list of includes, excludes, a base filter, and whether or not this filter should be "unsafe".
 
Filter "safety" is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.
 
If no base filter is specified, the default filter is assumed. When building a filter from scratch, the none built-in filter is useful.
 
When the size of the parameters being sent to this method grows to large, problems can occur. This method will accept POST requests to mitigate this.
 
It is not expected that many applications will call this method at runtime, filters should be pre-calculated and "baked in" in the common cases. Furthermore, there are a number of built-in filters which cover common use cases.
 
This method returns a single filter.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_filter_response = stackexchange.filter.create_filter(
    base="string_example",
    exclude="string_example",
    include="string_example",
    unsafe=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base: `str`<a id="base-str"></a>

##### exclude: `str`<a id="exclude-str"></a>

String list (semicolon delimited).

##### include: `str`<a id="include-str"></a>

String list (semicolon delimited).

##### unsafe: `bool`<a id="unsafe-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SingleFilter`](./stack_exchange_python_sdk/pydantic/single_filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/filters/create` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.filter.get_filter_details_by_ids`<a id="stackexchangefilterget_filter_details_by_ids"></a>

Returns the fields included by the given filters, and the "safeness" of those filters.
 
It is not expected that this method will be consumed by many applications at runtime, it is provided to aid in debugging.
 
{filters} can contain up to 20 semicolon delimited filters. Filters are obtained via calls to /filters/create, or by using a built-in filter.
 
This method returns a list of filters.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_filter_details_by_ids_response = stackexchange.filter.get_filter_details_by_ids(
    filters="filters_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: `str`<a id="filters-str"></a>

String list (semicolon delimited).

#### 🔄 Return<a id="🔄-return"></a>

[`Filters`](./stack_exchange_python_sdk/pydantic/filters.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/filters/{filters}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.information.get_statistics`<a id="stackexchangeinformationget_statistics"></a>

Returns a collection of statistics about the site.
 
Data to facilitate per-site customization, discover related sites, and aggregate statistics is all returned by this method.
 
This data is cached very aggressively, by design. Query sparingly, ideally no more than once an hour.
 
This method returns an info object.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_statistics_response = stackexchange.information.get_statistics(
    site="site_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

#### 🔄 Return<a id="🔄-return"></a>

[`InfoObject`](./stack_exchange_python_sdk/pydantic/info_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/info` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.information.get_tags_list`<a id="stackexchangeinformationget_tags_list"></a>

Returns the tags found on a site.
 
The inname parameter lets a consumer filter down to tags that contain a certain substring. For example, inname=own would return both "download" and "owner" amongst others.
 
This method returns a list of tags.
 
The sorts accepted by this method operate on the follow fields of the tag object:
 - popular - count
 - activity - the creation_date of the last question asked with the tag
 - name - name
  popular is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tags_list_response = stackexchange.information.get_tags_list(
    site="site_example",
    inname="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="popular",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### inname: `str`<a id="inname-str"></a>

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Tags`](./stack_exchange_python_sdk/pydantic/tags.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.mention.user_comments_list`<a id="stackexchangementionuser_comments_list"></a>

Returns the comments mentioning the user associated with the given access_token.
 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
user_comments_list_response = stackexchange.mention.user_comments_list(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/mentioned` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.merge.get_account_merge_list`<a id="stackexchangemergeget_account_merge_list"></a>

Returns a record of merges that have occurred involving a user identified by an access_token.
 
This method allows you to take now invalid account ids and find what account they've become, or take currently valid account ids and find which ids were equivalent in the past.
 
This is most useful when confirming that an account_id is in fact "new" to an application.
 
Account merges can happen for a wide range of reasons, applications should not make assumptions that merges have particular causes.
 
Note that accounts are managed at a network level, users on a site may be merged due to an account level merge but there is no guarantee that a merge has an effect on any particular site.
 
This method returns a list of account_merge.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_merge_list_response = stackexchange.merge.get_account_merge_list(
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`AccountMerge`](./stack_exchange_python_sdk/pydantic/account_merge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/merges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.message.get_inbox_items`<a id="stackexchangemessageget_inbox_items"></a>

Returns the user identified by access_token's inbox.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of inbox items.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_inbox_items_response = stackexchange.message.get_inbox_items(
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`InboxItems`](./stack_exchange_python_sdk/pydantic/inbox_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/inbox` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.message.get_unread_items`<a id="stackexchangemessageget_unread_items"></a>

Returns the unread items in a user's inbox.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of inbox items.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unread_items_response = stackexchange.message.get_unread_items(
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
    since=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### since: `int`<a id="since-int"></a>

Unix date.

#### 🔄 Return<a id="🔄-return"></a>

[`InboxItems`](./stack_exchange_python_sdk/pydantic/inbox_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inbox/unread` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.message.list_inbox_items`<a id="stackexchangemessagelist_inbox_items"></a>

Returns a user's inbox.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of inbox items.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_inbox_items_response = stackexchange.message.list_inbox_items(
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`InboxItems`](./stack_exchange_python_sdk/pydantic/inbox_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inbox` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.notification.get_unread_items_in_inbox`<a id="stackexchangenotificationget_unread_items_in_inbox"></a>

Returns the unread items in the user identified by access_token's inbox.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of inbox items.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unread_items_in_inbox_response = (
    stackexchange.notification.get_unread_items_in_inbox(
        site="site_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
        since=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### since: `int`<a id="since-int"></a>

Unix date.

#### 🔄 Return<a id="🔄-return"></a>

[`InboxItems`](./stack_exchange_python_sdk/pydantic/inbox_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/inbox/unread` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.notification.get_unread_items_in_inbox_0`<a id="stackexchangenotificationget_unread_items_in_inbox_0"></a>

Returns a user's unread notifications, given an access_token.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of notifications.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unread_items_in_inbox_0_response = (
    stackexchange.notification.get_unread_items_in_inbox_0(
        site="site_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Notifications`](./stack_exchange_python_sdk/pydantic/notifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/notifications/unread` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.notification.get_user_notifications`<a id="stackexchangenotificationget_user_notifications"></a>

Returns a user's notifications.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of notifications.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_notifications_response = stackexchange.notification.get_user_notifications(
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Notifications`](./stack_exchange_python_sdk/pydantic/notifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.notification.get_user_notifications_list`<a id="stackexchangenotificationget_user_notifications_list"></a>

Returns a user's notifications, given an access_token.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of notifications.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_notifications_list_response = (
    stackexchange.notification.get_user_notifications_list(
        site="site_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Notifications`](./stack_exchange_python_sdk/pydantic/notifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.notification.get_user_unread_notifications`<a id="stackexchangenotificationget_user_unread_notifications"></a>

Returns a user's unread notifications.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of notifications.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_unread_notifications_response = (
    stackexchange.notification.get_user_unread_notifications(
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Notifications`](./stack_exchange_python_sdk/pydantic/notifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/unread` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.permission.get_user_write_permissions`<a id="stackexchangepermissionget_user_write_permissions"></a>

Returns the write permissions a user has via the api, given an access token.
 
The Stack Exchange API gives users the ability to create, edit, and delete certain types. This method returns whether the passed user is capable of performing those actions at all, as well as how many times a day they can.
 
This method does not consider the user's current quota (ie. if they've already exhausted it for today) nor any additional restrictions on write access, such as editing deleted comments.
 
This method returns a list of write_permissions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_write_permissions_response = (
    stackexchange.permission.get_user_write_permissions(
        site="site_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`WritePermissions`](./stack_exchange_python_sdk/pydantic/write_permissions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/write-permissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.post.add_comment`<a id="stackexchangepostadd_comment"></a>

Create a new comment.
 
Use an access_token with write_access to create a new comment on a post.
 
This method returns the created comment.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_comment_response = stackexchange.post.add_comment(
    id=1,
    site="site_example",
    filter="string_example",
    param_callback="string_example",
    body="string_example",
    preview=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### body: `str`<a id="body-str"></a>

##### preview: `bool`<a id="preview-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CreatedComment`](./stack_exchange_python_sdk/pydantic/created_comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{id}/comments/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.post.comments_by_ids_get`<a id="stackexchangepostcomments_by_ids_get"></a>

Gets the comments on the posts identified in ids, regardless of the type of the posts.
 
This method is meant for cases when you are unsure of the type of the post id provided. Generally, this would be due to obtaining the post id directly from a user.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for post_id, answer_id, or question_id on post, answer, and question objects respectively.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
comments_by_ids_get_response = stackexchange.post.comments_by_ids_get(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{ids}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.post.get_all_posts`<a id="stackexchangepostget_all_posts"></a>

Fetches all posts (questions and answers) on the site.
 
In many ways this method is the union of /questions and /answers, returning both sets of data albeit only the common fields.
 
Most applications should use the question or answer specific methods, but /posts is available for those rare cases where any activity is of intereset. Examples of such queries would be: "all posts on Jan. 1st 2011" or "top 10 posts by score of all time".
 
The sorts accepted by this method operate on the follow fields of the post object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of posts.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_posts_response = stackexchange.post.get_all_posts(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Posts`](./stack_exchange_python_sdk/pydantic/posts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.post.get_post_revisions_by_ids`<a id="stackexchangepostget_post_revisions_by_ids"></a>

Returns edit revisions for the posts identified in ids.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for post_id, answer_id, or question_id on post, answer, and question objects respectively.
 
This method returns a list of revisions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_post_revisions_by_ids_response = stackexchange.post.get_post_revisions_by_ids(
    ids="ids_example",
    site="site_example",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Revisions`](./stack_exchange_python_sdk/pydantic/revisions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{ids}/revisions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.post.get_posts_by_ids`<a id="stackexchangepostget_posts_by_ids"></a>

Fetches a set of posts by ids.
 
This method is meant for grabbing an object when unsure whether an id identifies a question or an answer. This is most common with user entered data.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for post_id, answer_id, or question_id on post, answer, and question objects respectively.
 
The sorts accepted by this method operate on the follow fields of the post object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of posts.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_posts_by_ids_response = stackexchange.post.get_posts_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Posts`](./stack_exchange_python_sdk/pydantic/posts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.post.list_suggested_edits`<a id="stackexchangepostlist_suggested_edits"></a>

Returns suggsted edits on the posts identified in ids.
 
 - creation - creation_date
 - approval - approval_date
 - rejection - rejection_date
  creation is the default sort.
 
 {ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for post_id, answer_id, or question_id on post, answer, and question objects respectively.


 
This method returns a list of suggested-edits.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_suggested_edits_response = stackexchange.post.list_suggested_edits(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`SuggestedEdits`](./stack_exchange_python_sdk/pydantic/suggested_edits.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{ids}/suggested-edits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.privilege.get_earnable_list`<a id="stackexchangeprivilegeget_earnable_list"></a>

Returns the earnable privileges on a site.
 
Privileges define abilities a user can earn (via reputation) on any Stack Exchange site.
 
While fairly stable, over time they do change. New ones are introduced with new features, and the reputation requirements change as a site matures.
 
This method returns a list of privileges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_earnable_list_response = stackexchange.privilege.get_earnable_list(
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Privileges`](./stack_exchange_python_sdk/pydantic/privileges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/privileges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.privilege.get_user_privileges`<a id="stackexchangeprivilegeget_user_privileges"></a>

Returns the privileges the user identified by access_token has.
 
This method returns a list of privileges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_privileges_response = stackexchange.privilege.get_user_privileges(
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Privileges`](./stack_exchange_python_sdk/pydantic/privileges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/privileges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.query.similar_questions_search`<a id="stackexchangequerysimilar_questions_search"></a>

Returns questions which are similar to a hypothetical one based on a title and tag combination.
 
This method is roughly equivalent to a site's related questions suggestion on the ask page.
 
This method is useful for correlating data outside of a Stack Exchange site with similar content within one.
 
Note that title must always be passed as a parameter. tagged and nottagged are optional, semi-colon delimited lists of tags.
 
If tagged is passed it is treated as a preference, there is no guarantee that questions returned will have any of those tags. nottagged is treated as a requirement, no questions will be returned with those tags.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
 - relevance - order by "how similar" the questions are, most likely candidate first with a descending order Does not accept min or max
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
similar_questions_search_response = stackexchange.query.similar_questions_search(
    site="site_example",
    tagged="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
    nottagged="string_example",
    title="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### tagged: `str`<a id="tagged-str"></a>

String list (semicolon delimited).

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = relevance => none 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = relevance => none 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### nottagged: `str`<a id="nottagged-str"></a>

String list (semicolon delimited).

##### title: `str`<a id="title-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/similar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.query.site_questions_search`<a id="stackexchangequerysite_questions_search"></a>

Searches a site for any questions which fit the given criteria.
 
This method is intentionally quite limited. For more general searching, you should use a proper internet search engine restricted to the domain of the site in question.
 
At least one of tagged or intitle must be set on this method. nottagged is only used if tagged is also set, for performance reasons.
 
tagged and nottagged are semi-colon delimited list of tags. At least 1 tag in tagged will be on each returned question if it is passed, making it the OR equivalent of the AND version of tagged on /questions.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
 - relevance - matches the relevance tab on the site itself Does not accept min or max
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
site_questions_search_response = stackexchange.query.site_questions_search(
    site="site_example",
    tagged="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
    intitle="string_example",
    nottagged="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### tagged: `str`<a id="tagged-str"></a>

String list (semicolon delimited).

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = relevance => none 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = relevance => none 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### intitle: `str`<a id="intitle-str"></a>

##### nottagged: `str`<a id="nottagged-str"></a>

String list (semicolon delimited).

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.get_all_questions`<a id="stackexchangequestionget_all_questions"></a>

Gets all the questions on the site.
 
This method allows you make fairly flexible queries across the entire corpus of questions on a site. For example, getting all questions asked in the the week of Jan 1st 2011 with scores of 10 or more is a single query with parameters sort=votes&min=10&fromdate=1293840000&todate=1294444800.
 
To constrain questions returned to those with a set of tags, use the tagged parameter with a semi-colon delimited list of tags. This is an and contraint, passing tagged=c;java will return only those questions with both tags. As such, passing more than 5 tags will always return zero results.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
 - hot - by the formula ordering the hot tab Does not accept min or max
 - week - by the formula ordering the week tab Does not accept min or max
 - month - by the formula ordering the month tab Does not accept min or max
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_questions_response = stackexchange.question.get_all_questions(
    site="site_example",
    tagged="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### tagged: `str`<a id="tagged-str"></a>

String list (semicolon delimited).

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = hot => none sort = week => none sort = month => none sort = relevance => none 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = hot => none sort = week => none sort = month => none sort = relevance => none 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.get_by_ids`<a id="stackexchangequestionget_by_ids"></a>

Returns the questions identified in {ids}.
 
This is most useful for fetching fresh data when maintaining a cache of question ids, or polling for changes.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for question_id on question objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_ids_response = stackexchange.question.get_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.get_linked_questions`<a id="stackexchangequestionget_linked_questions"></a>

Gets questions which link to those questions identified in {ids}.
 
This method only considers questions that are linked within a site, and will never return questions from another Stack Exchange site.
 
A question is considered "linked" when it explicitly includes a hyperlink to another question, there are no other heuristics.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for question_id on question objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
 - rank - a priority sort by site applies, subject to change at any time Does not accept min or max
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_linked_questions_response = stackexchange.question.get_linked_questions(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = rank => none 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = rank => none 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/{ids}/linked` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.get_timeline_events`<a id="stackexchangequestionget_timeline_events"></a>

Returns a subset of the events that have happened to the questions identified in id.
 
This provides data similar to that found on a question's timeline page.
 
Voting data is scrubbed to deter inferencing of voter identity.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for question_id on question objects.
 
This method returns a list of question timeline events.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_timeline_events_response = stackexchange.question.get_timeline_events(
    ids="ids_example",
    site="site_example",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`QuestionTimelineEvents`](./stack_exchange_python_sdk/pydantic/question_timeline_events.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/{ids}/timeline` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.get_unaccepted_list`<a id="stackexchangequestionget_unaccepted_list"></a>

Returns the questions owned by the user associated with the given access_token that have no accepted answer.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unaccepted_list_response = stackexchange.question.get_unaccepted_list(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/questions/unaccepted` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.get_user_featured`<a id="stackexchangequestionget_user_featured"></a>

Returns the questions that have active bounties offered by the user associated with the given access_token.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_featured_response = stackexchange.question.get_user_featured(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/questions/featured` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.get_user_questions_list`<a id="stackexchangequestionget_user_questions_list"></a>

Returns the questions owned by the user associated with the given access_token.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_questions_list_response = stackexchange.question.get_user_questions_list(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.list_featured_questions`<a id="stackexchangequestionlist_featured_questions"></a>

Returns all the questions with active bounties in the system.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_featured_questions_response = stackexchange.question.list_featured_questions(
    site="site_example",
    tagged="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### tagged: `str`<a id="tagged-str"></a>

String list (semicolon delimited).

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/featured` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.question.list_related_questions`<a id="stackexchangequestionlist_related_questions"></a>

Returns questions that the site considers related to those identified in {ids}.
 
The algorithm for determining if questions are related is not documented, and subject to change at any time. Futhermore, these values are very heavily cached, and may not update immediately after a question has been editted. It is also not guaranteed that a question will be considered related to any number (even non-zero) of questions, and a consumer should be able to handle a variable number of returned questions.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for question_id on question objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
 - rank - a priority sort by site applies, subject to change at any time Does not accept min or max
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_related_questions_response = stackexchange.question.list_related_questions(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = rank => none 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = rank => none 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/questions/{ids}/related` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.reputation.get_full_history`<a id="stackexchangereputationget_full_history"></a>

Returns user's full reputation history, including private events.
 
 This method requires an access_token, with a scope containing "private_info".


 
This method returns a list of reputation_history.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_full_history_response = stackexchange.reputation.get_full_history(
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`ReputationHistory`](./stack_exchange_python_sdk/pydantic/reputation_history.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/reputation-history/full` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.reputation.get_user_reputation_changes`<a id="stackexchangereputationget_user_reputation_changes"></a>

Returns the reputation changed for the user associated with the given access_token.
 
This method returns a list of reputation changes.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_reputation_changes_response = (
    stackexchange.reputation.get_user_reputation_changes(
        site="site_example",
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`ReputationChanges`](./stack_exchange_python_sdk/pydantic/reputation_changes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/reputation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.reputation.get_user_reputation_history`<a id="stackexchangereputationget_user_reputation_history"></a>

Returns user's public reputation history.
 
This method returns a list of reputation_history.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_reputation_history_response = (
    stackexchange.reputation.get_user_reputation_history(
        site="site_example",
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`ReputationHistory`](./stack_exchange_python_sdk/pydantic/reputation_history.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/reputation-history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.revision.list_revisions_by_ids`<a id="stackexchangerevisionlist_revisions_by_ids"></a>

Returns edit revisions identified by ids in {ids}.
 
{ids} can contain up to 20 semicolon delimited ids, to find ids programatically look for revision_guid on revision objects. Note that unlike most other id types in the API, revision_guid is a string.
 
This method returns a list of revisions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_revisions_by_ids_response = stackexchange.revision.list_revisions_by_ids(
    ids="ids_example",
    site="site_example",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Guid list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Revisions`](./stack_exchange_python_sdk/pydantic/revisions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/revisions/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.search.site_questions_advanced_search`<a id="stackexchangesearchsite_questions_advanced_search"></a>

Searches a site for any questions which fit the given criteria.
 
Search criteria are expressed using the following parameters:
  - q - a free form text parameter, will match all question properties based on an undocumented algorithm.
 - accepted - true to return only questions with accepted answers, false to return only those without. Omit to elide constraint.
 - answers - the minimum number of answers returned questions must have.
 - body - text which must appear in returned questions' bodies.
 - closed - true to return only closed questions, false to return only open ones. Omit to elide constraint.
 - migrated - true to return only questions migrated away from a site, false to return only those not. Omit to elide constraint.
 - notice - true to return only questions with post notices, false to return only those without. Omit to elide constraint.
 - nottagged - a semicolon delimited list of tags, none of which will be present on returned questions.
 - tagged - a semicolon delimited list of tags, of which at least one will be present on all returned questions.
 - title - text which must appear in returned questions' titles.
 - user - the id of the user who must own the questions returned.
 - url - a url which must be contained in a post, may include a wildcard.
 - views - the minimum number of views returned questions must have.
 - wiki - true to return only community wiki questions, false to return only non-community wiki ones. Omit to elide constraint.


  
At least one additional parameter must be set if nottagged is set, for performance reasons.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
 - relevance - matches the relevance tab on the site itself Does not accept min or max
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
site_questions_advanced_search_response = (
    stackexchange.search.site_questions_advanced_search(
        site="site_example",
        tagged="string_example",
        order="desc",
        max="string_example",
        min="string_example",
        sort="activity",
        fromdate=1,
        todate=1,
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
        accepted="true",
        answers=1,
        body="string_example",
        closed="true",
        migrated="true",
        notice="true",
        nottagged="string_example",
        q="string_example",
        title="string_example",
        url="string_example",
        user=1,
        views=1,
        wiki="true",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### tagged: `str`<a id="tagged-str"></a>

String list (semicolon delimited).

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = relevance => none 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = relevance => none 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### accepted: `str`<a id="accepted-str"></a>

##### answers: `int`<a id="answers-int"></a>

##### body: `str`<a id="body-str"></a>

##### closed: `str`<a id="closed-str"></a>

##### migrated: `str`<a id="migrated-str"></a>

##### notice: `str`<a id="notice-str"></a>

##### nottagged: `str`<a id="nottagged-str"></a>

String list (semicolon delimited).

##### q: `str`<a id="q-str"></a>

##### title: `str`<a id="title-str"></a>

##### url: `str`<a id="url-str"></a>

##### user: `int`<a id="user-int"></a>

##### views: `int`<a id="views-int"></a>

##### wiki: `str`<a id="wiki-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/search/advanced` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.site.list_sites`<a id="stackexchangesitelist_sites"></a>

Returns all sites in the network.
 
This method allows for discovery of new sites, and changes to existing ones. Be aware that unlike normal API methods, this method should be fetched very infrequently, it is very unusual for these values to change more than once on any given day. It is suggested that you cache its return for at least one day, unless your app encounters evidence that it has changed (such as from the /info method).
 
The pagesize parameter for this method is unbounded, in acknowledgement that for many applications repeatedly fetching from /sites would complicate start-up tasks needlessly.
 
This method returns a list of sites.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sites_response = stackexchange.site.list_sites(
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Sites`](./stack_exchange_python_sdk/pydantic/sites.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sites` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_faq_questions`<a id="stackexchangetagget_faq_questions"></a>

Returns the frequently asked questions for the given set of tags in {tags}.
 
For a question to be returned, it must have all the tags in {tags} and be considered "frequently asked". The exact algorithm for determining whether a question is considered a FAQ is subject to change at any time.
 
{tags} can contain up to 5 individual tags per request.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_faq_questions_response = stackexchange.tag.get_faq_questions(
    tags="tags_example",
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tags}/faq` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_moderator_only_tags_list`<a id="stackexchangetagget_moderator_only_tags_list"></a>

Returns the tags found on a site that only moderators can use.
 
The inname parameter lets a consumer filter down to tags that contain a certain substring. For example, inname=own would return both "download" and "owner" amongst others.
 
This method returns a list of tags.
 
The sorts accepted by this method operate on the follow fields of the tag object:
 - popular - count
 - activity - the creation_date of the last question asked with the tag
 - name - name
  popular is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_moderator_only_tags_list_response = stackexchange.tag.get_moderator_only_tags_list(
    site="site_example",
    inname="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="popular",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### inname: `str`<a id="inname-str"></a>

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Tags`](./stack_exchange_python_sdk/pydantic/tags.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/moderator-only` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_related_tags`<a id="stackexchangetagget_related_tags"></a>

Returns the tags that are most related to those in {tags}.
 
Including multiple tags in {tags} is equivalent to asking for "tags related to tag #1 and tag #2" not "tags related to tag #1 or tag #2".
 
count on tag objects returned is the number of question with that tag that also share all those in {tags}.
 
{tags} can contain up to 4 individual tags per request.
 
This method returns a list of tags.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_related_tags_response = stackexchange.tag.get_related_tags(
    tags="tags_example",
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Tags`](./stack_exchange_python_sdk/pydantic/tags.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tags}/related` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_tag_info`<a id="stackexchangetagget_tag_info"></a>

Returns tag objects representing the tags in {tags} found on the site.
 
This method diverges from the standard naming patterns to avoid to conflicting with existing methods, due to the free form nature of tag names.
 
This method returns a list of tags.
 
The sorts accepted by this method operate on the follow fields of the tag object:
 - popular - count
 - activity - the creation_date of the last question asked with the tag
 - name - name
  popular is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tag_info_response = stackexchange.tag.get_tag_info(
    tags="tags_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="popular",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Tags`](./stack_exchange_python_sdk/pydantic/tags.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tags}/info` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_tag_wikis`<a id="stackexchangetagget_tag_wikis"></a>

Returns the wikis that go with the given set of tags in {tags}.
 
Be aware that not all tags have wikis.
 
{tags} can contain up to 20 individual tags per request.
 
This method returns a list of tag wikis.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tag_wikis_response = stackexchange.tag.get_tag_wikis(
    tags="tags_example",
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TagWikis`](./stack_exchange_python_sdk/pydantic/tag_wikis.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tags}/wikis` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_top_askers_by_period`<a id="stackexchangetagget_top_askers_by_period"></a>

Returns the top 30 askers active in a single tag, of either all-time or the last 30 days.
 
This is a view onto the data presented on the tag info page on the sites.
 
This method returns a list of tag score objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_askers_by_period_response = stackexchange.tag.get_top_askers_by_period(
    tag="tag_example",
    period="all_time",
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag: `str`<a id="tag-str"></a>

##### period: `str`<a id="period-str"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TagScoreObjects`](./stack_exchange_python_sdk/pydantic/tag_score_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag}/top-askers/{period}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_user_tags_list`<a id="stackexchangetagget_user_tags_list"></a>

Returns the tags the user identified by the access_token passed is active in.
 
This method returns a list of tags.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_tags_list_response = stackexchange.tag.get_user_tags_list(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="popular",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Tags`](./stack_exchange_python_sdk/pydantic/tags.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_user_top_questions`<a id="stackexchangetagget_user_top_questions"></a>

Returns the top 30 questions the user associated with the given access_token has posted in response to questions with the given tags.
 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_top_questions_response = stackexchange.tag.get_user_top_questions(
    tags="tags_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = hot => none sort = week => none sort = month => none sort = relevance => none 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = hot => none sort = week => none sort = month => none sort = relevance => none 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tags/{tags}/top-questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.get_user_top_tags_list`<a id="stackexchangetagget_user_top_tags_list"></a>

Returns the user identified by access_token's top 30 tags by question score.
 
This method returns a list of top tag objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_top_tags_list_response = stackexchange.tag.get_user_top_tags_list(
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TopTagObjects`](./stack_exchange_python_sdk/pydantic/top_tag_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/top-question-tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.list_required_tags`<a id="stackexchangetaglist_required_tags"></a>

Returns the tags found on a site that fulfill required tag constraints on questions.
 
The inname parameter lets a consumer filter down to tags that contain a certain substring. For example, inname=own would return both "download" and "owner" amongst others.
 
This method returns a list of tags.
 
The sorts accepted by this method operate on the follow fields of the tag object:
 - popular - count
 - activity - the creation_date of the last question asked with the tag
 - name - name
  popular is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_required_tags_response = stackexchange.tag.list_required_tags(
    site="site_example",
    inname="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="popular",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### inname: `str`<a id="inname-str"></a>

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Tags`](./stack_exchange_python_sdk/pydantic/tags.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/required` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.list_synonyms`<a id="stackexchangetaglist_synonyms"></a>

Gets all the synonyms that point to the tags identified in {tags}. If you're looking to discover all the tag synonyms on a site, use the /tags/synonyms methods instead of call this method on all tags.
 
{tags} can contain up to 20 individual tags per request.
 
The sorts accepted by this method operate on the follow fields of the tag_synonym object:
 - creation - creation_date
 - applied - applied_count
 - activity - last_applied_date
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of tag synonyms.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_synonyms_response = stackexchange.tag.list_synonyms(
    tags="tags_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = applied => number sort = activity => date 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = applied => number sort = activity => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TagSynonyms`](./stack_exchange_python_sdk/pydantic/tag_synonyms.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tags}/synonyms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.tag.synonyms_list`<a id="stackexchangetagsynonyms_list"></a>

Returns all tag synonyms found a site.
 
When searching for synonyms of specific tags, it is better to use /tags/{tags}/synonyms over this method.
 
The sorts accepted by this method operate on the follow fields of the tag_synonym object:
 - creation - creation_date
 - applied - applied_count
 - activity - last_applied_date
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of tag_synonyms.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synonyms_list_response = stackexchange.tag.synonyms_list(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = applied => number sort = activity => date 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = applied => number sort = activity => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TagSynonyms`](./stack_exchange_python_sdk/pydantic/tag_synonyms.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/synonyms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.timeline.get_user_timeline`<a id="stackexchangetimelineget_user_timeline"></a>

Returns a subset of the actions the user identified by the passed access_token has taken on the site.
 
This method returns a list of user timeline objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_timeline_response = stackexchange.timeline.get_user_timeline(
    site="site_example",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`UserTimelineObjects`](./stack_exchange_python_sdk/pydantic/user_timeline_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/timeline` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_associated_accounts`<a id="stackexchangeuserget_associated_accounts"></a>

Returns all of a user's associated accounts, given their account_ids in {ids}.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for account_id on user objects.
 
This method returns a list of network_users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_associated_accounts_response = stackexchange.user.get_associated_accounts(
    ids="ids_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkUsers`](./stack_exchange_python_sdk/pydantic/network_users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/associated` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_comments_by_ids`<a id="stackexchangeuserget_comments_by_ids"></a>

Get the comments posted by users in {ids}.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comments_by_ids_response = stackexchange.user.get_comments_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_favorites_list`<a id="stackexchangeuserget_favorites_list"></a>

Get the questions that users in {ids} have favorited.
 
This method is effectively a view onto a user's favorites tab.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
 - added - when the user favorited the question
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_favorites_list_response = stackexchange.user.get_favorites_list(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = added => date 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number sort = added => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/favorites` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_featured_questions`<a id="stackexchangeuserget_featured_questions"></a>

Gets the questions on which the users in {ids} have active bounties.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_featured_questions_response = stackexchange.user.get_featured_questions(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/questions/featured` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_full_reputation_history`<a id="stackexchangeuserget_full_reputation_history"></a>

Returns a user's full reputation history, including private events.
 
This method requires an access_token, with a scope containing "private_info".
 
This method returns a list of reputation_history.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_full_reputation_history_response = stackexchange.user.get_full_reputation_history(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`ReputationHistory`](./stack_exchange_python_sdk/pydantic/reputation_history.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/reputation-history/full` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_inbox_items`<a id="stackexchangeuserget_inbox_items"></a>

Returns a user's inbox.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method is effectively an alias for /inbox. It is provided for consumers who make strong assumptions about operating within the context of a single site rather than the Stack Exchange network as a whole.
 
{id} can contain a single id, to find it programatically look for user_id on user or shallow_user objects.
 
This method returns a list of inbox items.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_inbox_items_response = stackexchange.user.get_inbox_items(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`InboxItems`](./stack_exchange_python_sdk/pydantic/inbox_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/inbox` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_inbox_unread`<a id="stackexchangeuserget_inbox_unread"></a>

Returns the unread items in a user's inbox.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method is effectively an alias for /inbox/unread. It is provided for consumers who make strong assumptions about operating within the context of a single site rather than the Stack Exchange network as a whole.
 
{id} can contain a single id, to find it programatically look for user_id on user or shallow_user objects.
 
This method returns a list of inbox items.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_inbox_unread_response = stackexchange.user.get_inbox_unread(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
    since=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

##### since: `int`<a id="since-int"></a>

Unix date.

#### 🔄 Return<a id="🔄-return"></a>

[`InboxItems`](./stack_exchange_python_sdk/pydantic/inbox_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/inbox/unread` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_notifications_list`<a id="stackexchangeuserget_notifications_list"></a>

Returns a user's notifications.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of notifications.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_notifications_list_response = stackexchange.user.get_notifications_list(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Notifications`](./stack_exchange_python_sdk/pydantic/notifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_privileges_list`<a id="stackexchangeuserget_privileges_list"></a>

Returns the privileges a user has.
 
Applications are encouraged to calculate privileges themselves, without repeated queries to this method. A simple check against the results returned by /privileges and user.user_type would be sufficient.
 
{id} can contain only a single, to find it programatically look for user_id on user or shallow_user objects.
 
This method returns a list of privileges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_privileges_list_response = stackexchange.user.get_privileges_list(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Privileges`](./stack_exchange_python_sdk/pydantic/privileges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/privileges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_questions_by_user_ids`<a id="stackexchangeuserget_questions_by_user_ids"></a>

Gets the questions asked by the users in {ids}.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_questions_by_user_ids_response = stackexchange.user.get_questions_by_user_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_reputation_changes`<a id="stackexchangeuserget_reputation_changes"></a>

Gets a subset of the reputation changes for users in {ids}.
 
Reputation changes are intentionally scrubbed of some data to make it difficult to correlate votes on particular posts with user reputation changes. That being said, this method returns enough data for reasonable display of reputation trends.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
This method returns a list of reputation objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_reputation_changes_response = stackexchange.user.get_reputation_changes(
    ids="ids_example",
    site="site_example",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`ReputationChanges`](./stack_exchange_python_sdk/pydantic/reputation_changes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/reputation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_reputation_history`<a id="stackexchangeuserget_reputation_history"></a>

Returns users' public reputation history.
 
This method returns a list of reputation_history.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_reputation_history_response = stackexchange.user.get_reputation_history(
    ids="ids_example",
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`ReputationHistory`](./stack_exchange_python_sdk/pydantic/reputation_history.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/reputation-history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_suggested_edits_by_ids`<a id="stackexchangeuserget_suggested_edits_by_ids"></a>

Returns the suggested edits a users in {ids} have submitted.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the suggested_edit object:
 - creation - creation_date
 - approval - approval_date Does not return unapproved suggested_edits
 - rejection - rejection_date Does not return unrejected suggested_edits
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of suggested-edits.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_suggested_edits_by_ids_response = stackexchange.user.get_suggested_edits_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = approval => date sort = rejection => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`SuggestedEdits`](./stack_exchange_python_sdk/pydantic/suggested_edits.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/suggested-edits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_tags`<a id="stackexchangeuserget_tags"></a>

Returns the tags the users identified in {ids} have been active in.
 
This route corresponds roughly to user's stats tab, but does not include tag scores. A subset of tag scores are available (on a single user basis) in /users/{id}/top-answer-tags and /users/{id}/top-question-tags.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the tag object:
 - popular - count
 - activity - the creation_date of the last question asked with the tag
 - name - name
  popular is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of tags.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tags_response = stackexchange.user.get_tags(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="popular",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### min: `str`<a id="min-str"></a>

sort = popular => number sort = activity => date sort = name => string 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Tags`](./stack_exchange_python_sdk/pydantic/tags.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_top_question_tags`<a id="stackexchangeuserget_top_question_tags"></a>

Returns a single user's top tags by question score.
 
This a subset of the data returned on a user's tags tab.
 
{id} can contain a single id, to find it programatically look for user_id on user or shallow_user objects.
 
This method returns a list of top_tag objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_question_tags_response = stackexchange.user.get_top_question_tags(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TopTagObjects`](./stack_exchange_python_sdk/pydantic/top_tag_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/top-question-tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_top_questions_by_tags`<a id="stackexchangeuserget_top_questions_by_tags"></a>

Returns the top 30 questions a user has asked with the given tags.
 
{id} can contain a single id, to find it programatically look for user_id on user or shallow_user objects. {tags} is limited to 5 tags, passing more will result in an error.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_questions_by_tags_response = stackexchange.user.get_top_questions_by_tags(
    id=1,
    tags="tags_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/tags/{tags}/top-questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_unaccepted_questions`<a id="stackexchangeuserget_unaccepted_questions"></a>

Gets the questions asked by the users in {ids} which have at least one answer, but no accepted answer.
 
Questions returned by this method have answers, but the owner has not opted to accept any of them.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unaccepted_questions_response = stackexchange.user.get_unaccepted_questions(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/questions/unaccepted` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_unanswered_questions`<a id="stackexchangeuserget_unanswered_questions"></a>

Gets the questions asked by the users in {ids} which the site consideres unanswered, while still having at least one answer posted.
 
These rules are subject to change, but currently any question without at least one upvoted or accepted answer is considered unanswered.
 
To get the set of questions that a user probably considers unanswered, the returned questions should be unioned with those returned by /users/{id}/questions/no-answers. These methods are distinct so that truly unanswered (that is, zero posted answers) questions can be easily separated from mearly poorly or inadequately answered ones.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unanswered_questions_response = stackexchange.user.get_unanswered_questions(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/questions/unanswered` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_unread_notifications`<a id="stackexchangeuserget_unread_notifications"></a>

Returns a user's unread notifications.
 
This method requires an access_token, with a scope containing "read_inbox".
 
This method returns a list of notifications.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unread_notifications_response = stackexchange.user.get_unread_notifications(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Notifications`](./stack_exchange_python_sdk/pydantic/notifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/notifications/unread` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_user`<a id="stackexchangeuserget_user"></a>

Returns the user associated with the passed access_token.
 
This method returns a user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_response = stackexchange.user.get_user(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="reputation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### min: `str`<a id="min-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./stack_exchange_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_user_answers_list`<a id="stackexchangeuserget_user_answers_list"></a>

Returns the answers the users in {ids} have posted.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the answer object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of answers.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_answers_list_response = stackexchange.user.get_user_answers_list(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Answers`](./stack_exchange_python_sdk/pydantic/answers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_user_comments_by_ids_and_toid`<a id="stackexchangeuserget_user_comments_by_ids_and_toid"></a>

Get the comments that the users in {ids} have posted in reply to the single user identified in {toid}.
 
This method is useful for extracting conversations, especially over time or across multiple posts.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects. {toid} can contain only 1 id, found in the same manner as those in {ids}.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  creation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_comments_by_ids_and_toid_response = (
    stackexchange.user.get_user_comments_by_ids_and_toid(
        ids="ids_example",
        toid=1,
        site="site_example",
        order="desc",
        max="string_example",
        min="string_example",
        sort="creation",
        fromdate=1,
        todate=1,
        pagesize=1,
        page=1,
        filter="string_example",
        param_callback="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### toid: `int`<a id="toid-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/comments/{toid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_user_profiles_by_ids`<a id="stackexchangeuserget_user_profiles_by_ids"></a>

Gets the users identified in ids in {ids}.
 
Typically this method will be called to fetch user profiles when you have obtained user ids from some other source, such as /questions.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the user object:
 - reputation - reputation
 - creation - creation_date
 - name - display_name
 - modified - last_modified_date
  reputation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_profiles_by_ids_response = stackexchange.user.get_user_profiles_by_ids(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="reputation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### min: `str`<a id="min-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./stack_exchange_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_user_timeline_by_ids`<a id="stackexchangeuserget_user_timeline_by_ids"></a>

Returns a subset of the actions the users in {ids} have taken on the site.
 
This method returns users' posts, edits, and earned badges in the order they were accomplished. It is possible to filter to just a window of activity using the fromdate and todate parameters.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
This method returns a list of user timeline objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_timeline_by_ids_response = stackexchange.user.get_user_timeline_by_ids(
    ids="ids_example",
    site="site_example",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`UserTimelineObjects`](./stack_exchange_python_sdk/pydantic/user_timeline_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/timeline` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_user_top_answer_tags`<a id="stackexchangeuserget_user_top_answer_tags"></a>

Returns a single user's top tags by answer score.
 
This a subset of the data returned on a user's tags tab.
 
{id} can contain a single id, to find it programatically look for user_id on user or shallow_user objects.
 
This method returns a list of top_tag objects.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_top_answer_tags_response = stackexchange.user.get_user_top_answer_tags(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`TopTagObjects`](./stack_exchange_python_sdk/pydantic/top_tag_objects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/top-answer-tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_user_top_answers`<a id="stackexchangeuserget_user_top_answers"></a>

Returns the top 30 answers a user has posted in response to questions with the given tags.
 
{id} can contain a single id, to find it programatically look for user_id on user or shallow_user objects. {tags} is limited to 5 tags, passing more will result in an error.
 
The sorts accepted by this method operate on the follow fields of the answer object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of answers.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_top_answers_response = stackexchange.user.get_user_top_answers(
    id=1,
    tags="tags_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### tags: `str`<a id="tags-str"></a>

String list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Answers`](./stack_exchange_python_sdk/pydantic/answers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/tags/{tags}/top-answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.get_write_permissions`<a id="stackexchangeuserget_write_permissions"></a>

Returns the write permissions a user has via the api.
 
The Stack Exchange API gives users the ability to create, edit, and delete certain types. This method returns whether the passed user is capable of performing those actions at all, as well as how many times a day they can.
 
This method does not consider the user's current quota (ie. if they've already exhausted it for today) nor any additional restrictions on write access, such as editing deleted comments.
 
This method returns a list of write_permissions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_write_permissions_response = stackexchange.user.get_write_permissions(
    id=1,
    site="site_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`WritePermissions`](./stack_exchange_python_sdk/pydantic/write_permissions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/write-permissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.list_account_merges`<a id="stackexchangeuserlist_account_merges"></a>

Returns a record of merges that have occurred involving the passed account ids.
 
This method allows you to take now invalid account ids and find what account they've become, or take currently valid account ids and find which ids were equivalent in the past.
 
This is most useful when confirming that an account_id is in fact "new" to an application.
 
Account merges can happen for a wide range of reasons, applications should not make assumptions that merges have particular causes.
 
Note that accounts are managed at a network level, users on a site may be merged due to an account level merge but there is no guarantee that a merge has an effect on any particular site.
 
This method returns a list of account_merge.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_account_merges_response = stackexchange.user.list_account_merges(
    ids="ids_example",
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`AccountMerge`](./stack_exchange_python_sdk/pydantic/account_merge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/merges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.list_elected_moderator_users`<a id="stackexchangeuserlist_elected_moderator_users"></a>

Returns those users on a site who both have moderator powers, and were actually elected.
 
This method excludes Stack Exchange Inc. employees, unless they were actually elected moderators on a site (which can only have happened prior to their employment).
 
The sorts accepted by this method operate on the follow fields of the user object:
 - reputation - reputation
 - creation - creation_date
 - name - display_name
 - modified - last_modified_date
  reputation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_elected_moderator_users_response = stackexchange.user.list_elected_moderator_users(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="reputation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### min: `str`<a id="min-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./stack_exchange_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/moderators/elected` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.list_moderator_users`<a id="stackexchangeuserlist_moderator_users"></a>

Gets those users on a site who can exercise moderation powers.
 
Note, employees of Stack Exchange Inc. will be returned if they have been granted moderation powers on a site even if they have never been appointed or elected explicitly. This method checks abilities, not the manner in which they were obtained.
 
The sorts accepted by this method operate on the follow fields of the user object:
 - reputation - reputation
 - creation - creation_date
 - name - display_name
 - modified - last_modified_date
  reputation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_moderator_users_response = stackexchange.user.list_moderator_users(
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="reputation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### min: `str`<a id="min-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./stack_exchange_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/moderators` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.list_no_answer_questions`<a id="stackexchangeuserlist_no_answer_questions"></a>

Gets the questions asked by the users in {ids} which have no answers.
 
Questions returns by this method actually have zero undeleted answers. It is completely disjoint /users/{ids}/questions/unanswered and /users/{ids}/questions/unaccepted, which only return questions with at least one answer, subject to other contraints.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the question object:
 - activity - last_activity_date
 - creation - creation_date
 - votes - score
  activity is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of questions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_no_answer_questions_response = stackexchange.user.list_no_answer_questions(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="activity",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = activity => date sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Questions`](./stack_exchange_python_sdk/pydantic/questions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/questions/no-answers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.list_user_badges`<a id="stackexchangeuserlist_user_badges"></a>

Get the badges the users in {ids} have earned.
 
Badge sorts are a tad complicated. For the purposes of sorting (and min/max) tag_based is considered to be greater than named.
 
This means that you can get a list of all tag based badges a user has by passing min=tag_based, and conversely all the named badges by passing max=named, with sort=type.
 
For ranks, bronze is greater than silver which is greater than gold. Along with sort=rank, set max=gold for just gold badges, max=silver&min=silver for just silver, and min=bronze for just bronze.
 
rank is the default sort.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
This method returns a list of badges.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_badges_response = stackexchange.user.list_user_badges(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="rank",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = rank => string sort = name => string sort = type => string sort = awarded => date 

##### min: `str`<a id="min-str"></a>

sort = rank => string sort = name => string sort = type => string sort = awarded => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Badges`](./stack_exchange_python_sdk/pydantic/badges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/badges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.list_users`<a id="stackexchangeuserlist_users"></a>

Returns all users on a site.
 
This method returns a list of users.
 
The sorts accepted by this method operate on the follow fields of the user object:
 - reputation - reputation
 - creation - creation_date
 - name - display_name
 - modified - last_modified_date
  reputation is the default sort.
 
 It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
The inname parameter lets consumers filter the results down to just those users with a certain substring in their display name. For example, inname=kevin will return all users with both users named simply "Kevin" or those with Kevin as one of (or part of) their names; such as "Kevin Montrose".


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_users_response = stackexchange.user.list_users(
    site="site_example",
    inname="string_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="reputation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### inname: `str`<a id="inname-str"></a>

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### min: `str`<a id="min-str"></a>

sort = reputation => number sort = creation => date sort = name => string sort = modified => date 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./stack_exchange_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `stackexchange.user.mentioned_comments_list`<a id="stackexchangeusermentioned_comments_list"></a>

Gets all the comments that the users in {ids} were mentioned in.
 
Note, to count as a mention the comment must be considered to be "in reply to" a user. Most importantly, this means that a comment can only be in reply to a single user.
 
{ids} can contain up to 100 semicolon delimited ids, to find ids programatically look for user_id on user or shallow_user objects.
 
The sorts accepted by this method operate on the follow fields of the comment object:
 - creation - creation_date
 - votes - score
  It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


 
This method returns a list of comments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mentioned_comments_list_response = stackexchange.user.mentioned_comments_list(
    ids="ids_example",
    site="site_example",
    order="desc",
    max="string_example",
    min="string_example",
    sort="creation",
    fromdate=1,
    todate=1,
    pagesize=1,
    page=1,
    filter="string_example",
    param_callback="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Number list (semicolon delimited).

##### site: `str`<a id="site-str"></a>

Each of these methods operates on a single site at a time, identified by the site parameter. This parameter can be the full domain name (ie. \"stackoverflow.com\"), or a short form identified by api_site_parameter on the site object. 

##### order: `str`<a id="order-str"></a>

##### max: `str`<a id="max-str"></a>

sort = creation => date sort = votes => number 

##### min: `str`<a id="min-str"></a>

sort = creation => date sort = votes => number 

##### sort: `str`<a id="sort-str"></a>

##### fromdate: `int`<a id="fromdate-int"></a>

Unix date.

##### todate: `int`<a id="todate-int"></a>

Unix date.

##### pagesize: `int`<a id="pagesize-int"></a>

##### page: `int`<a id="page-int"></a>

##### filter: `str`<a id="filter-str"></a>

#Discussion  The Stack Exchange API allows applications to exclude almost every field returned. For example, if an application did not care about a user's badge counts it could exclude user.badge_counts whenever it calls a method that returns users.  An application excludes fields by creating a filter (via /filter/create) and passing it to a method in the filter parameter.  Filters are immutable and non-expiring. An application can safely \"bake in\" any filters that are created, it is not necessary (or advisable) to create filters at runtime.  The motivation for filters are several fold. Filters allow applications to reduce API responses to just the fields they are concerned with, saving bandwidth. With the list of fields an application is actually concerned with, the API can avoid unneccessary queries thereby decreasing response time (and reducing load on our infrastructure). Finally, filters allow us to be more conservative in what the API returns by default without a proliferation of parameters (as was seen with body, answers, and comments in the 1.x API family).  #Safety  Filters also carry a notion of safety, which is defined as follows. Any string returned as a result of an API call with a safe filter will be inline-able into HTML without script-injection concerns. That is to say, no additional sanitizing (encoding, HTML tag stripping, etc.) will be necessary on returned strings. Applications that wish to handle sanitizing themselves should create an unsafe filter. All filters are safe by default, under the assumption that double-encoding bugs are more desirable than script injections.  Note that this does not mean that \"safe\" filter is mearly an \"unsafe\" one with all fields passed though UrlEncode(...). Many fields can and will contain HTML in all filter types (most notably, the *.body fields).  When using unsafe filters, the API returns the highest fidelity data it can reasonably access for the given request. This means that in cases where the \"safe\" data is the only accessible data it will be returned even in \"unsafe\" filters. Notably the *.body fields are unchanged, as they are stored in that form. Fields that are unchanged between safe and unsafe filters are denoted in their types documentation.  #Built In Filters  The following filters are built in:  default, each type documents which fields are returned under the default filter (for example, answers). withbody, which is default plus the *.body fields none, which is empty total, which includes just .total  #Compatibility with V1.x  For ease of transition from earlier API versions, the filters _b, _ba, _bc, _bca, _a, _ac, and _c are also built in. These are unsafe, and exclude a combination of question and answer body, comments, and answers so as to mimic the body, answers, and comments parameters that have been removed in V2.0. New applications should not use these filters. 

##### param_callback: `str`<a id="param_callback-str"></a>

All API responses are JSON, we do support JSONP with the callback query parameter. 

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./stack_exchange_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{ids}/mentioned` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
