import endpoints
from .messages import UserMessage
from .util import copy_attrs
from .models import User
from .exceptions import ConflictException, NotFoundException
from api import api_collection
from google.appengine.ext import ndb
from protorpc import message_types, messages, remote


class CurrentUserRequest(messages.Message):
    content = messages.StringField(1)


CURRENT_USER_RESOURCE = endpoints.ResourceContainer(CurrentUserRequest)

USER_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    username=messages.StringField(2, required=True))


@api_collection.api_class(resource_name='users')
class UsersApi(remote.Service):

    @endpoints.method(
        message_types.VoidMessage,
        UserMessage,
        path='@me',
        http_method='GET')
    def get_current_user(self, request):
        return UserMessage.from_model(User.get_current_user(),
                                      include_email=True)

    @endpoints.method(
        CURRENT_USER_RESOURCE,
        UserMessage,
        path='@me',
        http_method='POST')
    @ndb.transactional
    def create_current_user(self, request):
        user_obj = endpoints.get_current_user()
        ConflictException.raise_if_exists(User.get_key(user_obj))
        user = User.create_user(user_obj)
        user.put()
        return UserMessage.from_model(user, include_email=True)

    @endpoints.method(
        CURRENT_USER_RESOURCE,
        UserMessage,
        path='@me',
        http_method='PUT')
    def update_current_user(self, request):
        user_key = User.get_key(endpoints.get_current_user())
        user = NotFoundException.raise_if_not_exists(user_key)
        # TODO(james7132): Update user
        user.put()
        return UserMessage(user, include_email=True)

    @endpoints.method(
        message_types.VoidMessage,
        message_types.VoidMessage,
        path='@me',
        http_method='DELETE')
    @ndb.transactional
    def delete_current_user(self, request):
        user_key = User.get_key(endpoints.get_current_user())
        NotFoundException.raise_if_not_exists(user_key)
        # TODO(james7132): Delete the entire ancestor key tree under the circle
        # TODO(james7132): Delete all circle members
        user_key.delete()

    @endpoints.method(
        USER_RESOURCE,
        UserMessage,
        path='users/{username}',
        http_method='GET')
    def get_user(self, request):
        user = User.get_by_name(request.username)
        if not user:
            msg = 'A user with the username {} does not exist.'.format(
                username)
            raise NotFoundException(msg)
        return UserMessage.from_model(user)
