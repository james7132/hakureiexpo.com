import endpoints
from api import api_collection
from protorpc import message_types, messages, remote


class CircleResponse(messages.Message):
    created_at = message_types.DateTimeField(1, required=True)
    last_updated = message_types.DateTimeField(2, required=True)
    id = message_types.DateTimeField(3, required=True)
    name = messages.StringField(4, required=True)
    display_name = messages.StringField(5, required=False)
    bio = messages.StringField(6, required=False)
    email = messages.StringField(7, required=False)

CIRCLE_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        name=messages.StringField(2, required=False))

CIRCLE_MEMBER_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        name=messages.StringField(2, required=False),
        member_username=messages.StringField(3, required=True))

@api_collection.api_class(resource_name='circles')
class CirclesApi(remote.Service):

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleResponse,
        path='circles',
        http_method='POST')
    def create_circle(self, request):
        user = endpoints.get_user()
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleResponse,
        path='circles/{name}',
        http_method='GET')
    def get_circle(self, request):
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleResponse,
        path='circles/{name}',
        http_method='PUT')
    def update_circle(self, request):
        user = endpoints.get_user()
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleResponse,
        path='circles/{name}',
        http_method='DELETE')
    def delete_circle(self, request):
        user = endpoints.get_user()
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_RESOURCE,
        CircleResponse,
        path='circles/{name}/members',
        http_method='GET')
    def list_circle_members(self, request):
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        CircleResponse,
        path='circles/{name}/members',
        http_method='POST')
    def create_circle_member(self, request):
        user = endpoints.get_user()
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        CircleResponse,
        path='circles/{name}/members/{member_username}',
        http_method='GET')
    def get_circle_member(self, request):
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        CircleResponse,
        path='circles/{name}/members/{member_username}',
        http_method='PUT')
    def update_circle_member(self, request):
        user = endpoints.get_user()
        return CircleResponse(content=request.content)

    @endpoints.method(
        CIRCLE_MEMBER_RESOURCE,
        CircleResponse,
        path='circles/{name}/members/{member_username}',
        http_method='DELETE')
    def delete_circle_member(self, request):
        user = endpoints.get_user()
        return CircleResponse(content=request.content)
