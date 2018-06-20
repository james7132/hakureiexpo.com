import endpoints
from .models import Circle, User
from api import api_collection
from protorpc import message_types, messages, remote


class PostResponse(messages.Message):
    created_at = message_types.DateTimeField(1, required=True)
    last_updated = message_types.DateTimeField(2, required=True)
    author = messages.StringField(3, required=True)
    author_id = messages.StringField(4, required=True)
    id = message_types.DateTimeField(5, required=True)
    published = message_types.DateTimeField(6, required=False)
    description = messages.StringField(7, required=False)


class PostSummary(messages.Message):
    id = messages.StringField(1)
    description = messages.StringField(2)


class PostListResponse(messages.Message):
    author_id = messages.StringField(1)
    posts = messages.MessageField(PostSummary, 2, repeated=True)


POST_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    author=messages.StringField(2, required=True),
    post_id=messages.StringField(3, required=False))


def post_api(root_model_class, root):

    @api_collection.api_class(resource_name=root)
    class PostsApi(remote.Service):

        @endpoints.method(
            POST_RESOURCE,
            PostListResponse,
            path=root + '/{author}/posts',
            http_method='GET')
        def list_user_posts(self, request):
            return PostResponse(content=request.content)

        @endpoints.method(
            POST_RESOURCE,
            PostResponse,
            path=root + '/{author}/posts',
            http_method='POST')
        def create_user_post(self, request):
            user = endpoints.get_user()
            return PostResponse(content=request.content)

        @endpoints.method(
            POST_RESOURCE,
            PostResponse,
            path=root + '/{author}/posts/{post_id}',
            http_method='GET')
        def get_user_post(self, request):
            return PostResponse(content=request.content)

        @endpoints.method(
            POST_RESOURCE,
            PostResponse,
            path=root + '/{author}/posts/{post_id}',
            http_method='PUT')
        def update_user_post(self, request):
            user = endpoints.get_user()
            return PostResponse(content=request.content)

        @endpoints.method(
            POST_RESOURCE,
            message_types.VoidMessage,
            path=root + '/{author}/posts/{post_id}',
            http_method='DELETE')
        def delete_user_post(self, request):
            user = endpoints.get_user()
            return PostResponse(content=request.content)

    PostsApi.__name__ = root_model_class.__name__ + PostsApi.__name__
    return PostsApi


UserPostsApi = post_api(User, 'users')
CirclePostsApi = post_api(Circle, 'circles')
