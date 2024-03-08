# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from stack_exchange_python_sdk.paths.posts_ids_suggested_edits import Api

from stack_exchange_python_sdk.paths import PathValues

path = PathValues.POSTS_IDS_SUGGESTEDEDITS