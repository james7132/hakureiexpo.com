import endpoints
from api import api_collection
from protorpc import message_types, messages, remote


class CurrentUserRequest(messages.Message):
    content = messages.StringField(1)

class CurrentUserResponse(messages.Message):
    content = messages.StringField(1)

class UserResponse(messages.Message):
    content = messages.StringField(1)

class UserPostResponse(messages.Message):
    content = messages.StringField(1)


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
        CurrentUserResponse,
        path='@me',
        http_method='GET')
    def get_current_user(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        CURRENT_USER_RESOURCE,
        CurrentUserResponse,
        path='@me',
        http_method='POST')
    def create_current_user(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        CURRENT_USER_RESOURCE,
        CurrentUserResponse,
        path='@me',
        http_method='PUT')
    def update_current_user(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        message_types.VoidMessage,
        message_types.VoidMessage,
        path='@me',
        http_method='DELETE')
    def delete_current_user(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        USER_RESOURCE,
        UserResponse,
        path='{username}',
        http_method='GET')
    def get_user(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        USER_RESOURCE,
        UserResponse,
        path='{username}/posts',
        http_method='GET')
    def list_user_posts(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        UserResponse,
        path='{username}/posts',
        http_method='POST')
    def create_user_post(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        UserResponse,
        path='{username}/posts/{post_id}',
        http_method='GET')
    def get_user_post(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        UserResponse,
        path='{username}/posts/{post_id}',
        http_method='PUT')
    def update_user_post(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        USER_POST_RESOURCE,
        UserResponse,
        path='{username}/posts/{post_id}',
        http_method='DELETE')
    def delete_user_post(self, request):
        return CurrentUserResponse(content=request.content)
