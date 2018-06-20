import endpoints
from .messages import CircleMessage, CircleMemberMessage, CircleMemberListMessage
from .models import Circle, CircleMember
from api import api_collection
from google.appengine.ext import ndb
from protorpc import message_types, messages, remote


CIRCLE_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    name=messages.StringField(2, required=False))

CIRCLE_MEMBER_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    name=messages.StringField(2, required=False),
    member_username=messages.StringField(3, required=True))

CIRCLE_MEMBERS_PER_RESPONSE = 20


@api_collection.api_class(resource_name='circles')
class CirclesApi(remote.Service):

    def _authorize_user(self, circle):
        user = User.get_current_user()
        member = circle.get_member(user)
        if not member.is_owner:
            msg = 'User is not authorized to make changes to this circle.'
            raise endpoints.ForbiddenException(msg)

    def _get_member(self, name, member_name):
        circle = Circle.get_by_name(name)
        user = User.get_byname(name)
        return circle.get_member(user)

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleMessage,
        path='circles',
        http_method='POST')
    @ndb.transactional
    def create_circle(self, request):
        owner = User.get_current_user()
        circle = Circle(name='Test')  # TODO(james7132): Remove placeholder
        owner_member = circle.create_member(owner).populate(is_owner=True)
        circle.put()
        owner_menber.put()
        return circle.to_message()

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleMessage,
        path='circles/{name}',
        http_method='GET')
    def get_circle(self, request):
        circle = Circle.get_by_name(name)
        return circle.to_message()

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleMessage,
        path='circles/{name}',
        http_method='PUT')
    def update_circle(self, request):
        circle = Circle.get_by_name(name)
        self._authorize_user(circle)
        # TODO(james7132): Update circle
        circle.put()
        return circle.to_message()

    @endpoints.method(
        CIRCLE_RESOURCE,
        message_types.VoidMessage,
        path='circles/{name}',
        http_method='DELETE')
    def delete_circle(self, request):
        circle = Circle.get_by_name(name)
        self._authorize_user(circle)
        # TODO(james7132): Delete the entire ancestor key tree under the circle
        circle.key.delete()

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleMessage,
        path='circles/{name}/members',
        http_method='GET')
    def list_circle_members(self, request):
        circle = Circle.get_by_name(name)
        members = circle.query_members().fetch(CIRCLE_MEMBERS_PER_RESPONSE)
        return CircleMember.to_list_message(circle, members)

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        CircleMemberMessage,
        path='circles/{name}/members',
        http_method='POST')
    def create_circle_member(self, request):
        circle = Circle.get_by_name(name)
        # TODO(james7132): Remove this placeholder
        user = endpoints.get_current_user() 
        member = circle.create_member(user)
        return member.to_message()

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        CircleMemberMessage,
        path='circles/{name}/members/{member_username}',
        http_method='GET')
    def get_circle_member(self, request):
        member = self._get_member(request.name, request.member_username)
        return member.to_message()

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        CircleMemberMessage,
        path='circles/{name}/members/{member_username}',
        http_method='PUT')
    def update_circle_member(self, request):
        member = self._get_member(request.name, request.member_username)
        # TODO(james7132): Update member
        member.put()
        return member.to_message()

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        message_types.VoidMessage,
        path='circles/{name}/members/{member_username}',
        http_method='DELETE')
    def delete_circle_member(self, request):
        member = self._get_member(request.name, request.member_username)
        member.key.delete()
