import endpoints
from api import api_collection
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


@api_collection.api_class(resource_name='users')
class UsersApi(remote.Service):

    # @endpoints.method(
        # CURRENT_USER_RESOURCE,
        # CurrentUserResponse,
        # path='@me',
        # http_method='GET')
    # def get_current_user(self, request):
        # return CurrentUserResponse(content=request.content)


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
        CURRENT_USER_RESOURCE,
        CurrentUserResponse,
        path='@me',
        http_method='DELETE')
    def delete_current_user(self, request):
        return CurrentUserResponse(content=request.content)


    # @endpoints.method(
        # USER_RESOURCE,
        # UserResponse,
        # path='users',
        # http_method='GET')
    # def get_user(self, request):
        # return CurrentUserResponse(content=request.content)
