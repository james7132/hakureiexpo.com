import endpoints
from api import api_collection
from protorpc import message_types, messages, remote


class CurrentUserRequest(messages.Message):
    content = messages.StringField(1)

class UserResponse(messages.Message):
    created_at = message_types.DateTimeField(1, required=True)
    last_updated = message_types.DateTimeField(2, required=True)
    id = message_types.DateTimeField(3, required=True)
    username = messages.StringField(4, required=True)
    display_name = messages.StringField(5, required=False)
    bio = messages.StringField(6, required=False)
    email = messages.StringField(7, required=False)

class UserPostResponse(messages.Message):
    created_at = message_types.DateTimeField(1, required=True)
    last_updated = message_types.DateTimeField(2, required=True)
    author = messages.StringField(3, required=True)
    author_id = messages.StringField(4, required=True)
    id = message_types.DateTimeField(5, required=True)
    published = message_types.DateTimeField(6, required=False)
    description = messages.StringField(7, required=False)

class UserPostSummary(messages.Message):
    id = messages.StringField(1)
    description = messages.StringField(2)

class UserPostListResponse(messages.Message):
    posts = messages.MessageField(UserPostSummary, 1, repeated=True)


CURRENT_USER_RESOURCE = endpoints.ResourceContainer(CurrentUserRequest)

USER_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        username=messages.StringField(2, required=True))

USER_POST_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        username=messages.StringField(2, required=True),
        post_id=messages.IntegerField(3, variant=messages.Variant.INT32,
                                      required=False))


@api_collection.api_class(resource_name='users')
class UsersApi(remote.Service):

    @endpoints.method(
        message_types.VoidMessage,
        UserResponse,
        path='@me',
        http_method='GET')
    def get_current_user(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        CURRENT_USER_RESOURCE,
        UserResponse,
        path='@me',
        http_method='POST')
    def create_current_user(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        CURRENT_USER_RESOURCE,
        UserResponse,
        path='@me',
        http_method='PUT')
    def update_current_user(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        message_types.VoidMessage,
        message_types.VoidMessage,
        path='@me',
        http_method='DELETE')
    def delete_current_user(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        USER_RESOURCE,
        UserResponse,
        path='users/{username}',
        http_method='GET')
    def get_user(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        USER_RESOURCE,
        UserPostListResponse,
        path='users/{username}/posts',
        http_method='GET')
    def list_user_posts(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        UserResponse,
        path='users/{username}/posts',
        http_method='POST')
    def create_user_post(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        UserPostResponse,
        path='users/{username}/posts/{post_id}',
        http_method='GET')
    def get_user_post(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        UserPostResponse,
        path='users/{username}/posts/{post_id}',
        http_method='PUT')
    def update_user_post(self, request):
        return UserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        message_types.VoidMessage,
        path='users/{username}/posts/{post_id}',
        http_method='DELETE')
    def delete_user_post(self, request):
        return UserResponse(content=request.content)
