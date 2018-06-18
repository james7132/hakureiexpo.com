import endpoints
from protorpc import message_types, messages, remote


class CurrentUserRequest(messages.Message):
    content = messages.StringField(1)


class CurrentUserResponse(messages.Message):
    content = messages.StringField(1)


class UserRequest(messages.Message):
    content = messages.StringField(1)


class UserResponse(messages.Message):
    content = messages.StringField(1)


CURRENT_USER_RESOURCE = endpoints.ResourceContainer(CurrentUserRequest)
USER_RESOURCE = endpoints.ResourceContainer(UserRequest)


@endpoints.api(name='users', version='v1')
class UsersApi(remote.Service):

    @endpoints.method(
        CURRENT_USER_RESOURCE,
        CurrentUserResponse,
        path='@me',
        http_method='GET',
        name='current_user')
    def get_current_user(self, request):
        return CurrentUserResponse(content=request.content)


    @endpoints.method(
        CURRENT_USER_RESOURCE,
        CurrentUserResponse,
        path='@me',
        http_method='POST',
        name='current_user')
    def create_current_user(self, request):
        return CurrentUserResponse(content=request.content)


    @endpoints.method(
        CURRENT_USER_RESOURCE,
        CurrentUserResponse,
        path='@me',
        http_method='PUT',
        name='current_user')
    def update_current_user(self, request):
        return CurrentUserResponse(content=request.content)


    @endpoints.method(
        CURRENT_USER_RESOURCE,
        VoidResponse,
        path='@me',
        http_method='DELETE',
        name='current_user')
    def delete_current_user(self, request):
        return CurrentUserResponse(content=request.content)

    @endpoints.method(
        USER_RESOURCE,
        UserResponse,
        path='users',
        http_method='GET',
        name='current_user')
    def get_current_user(self, request):
        return CurrentUserResponse(content=request.content)


