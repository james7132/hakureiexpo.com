import endpoints
from .messages import PostMessage, PostListMessage
from .util import copy_attrs
from .models import Circle, User
from api import api_collection
from google.appengine.ext import ndb
from protorpc import message_types, messages, remote



POST_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    author=messages.StringField(2, required=True),
    post_id=messages.StringField(3, required=False))

POSTS_PER_RESPONSE = 20


def post_api(root_model_class, root):

    @api_collection.api_class(resource_name=root)
    class PostsApi(remote.Service):

        @endpoints.method(
            POST_RESOURCE,
            PostListMessage,
            path=root + '/{author}/posts',
            http_method='GET')
        def list_user_posts(self, request):
            account = root_model_class.get_by_name(request.author)
            if not account:
                raise NotFoundException('Author not found')
            posts = account.query_posts().fetch(POSTS_PER_RESPONSE)
            return PostListMessage.to_summaries(account, posts)

        @endpoints.method(
            POST_RESOURCE,
            PostMessage,
            path=root + '/{author}/posts',
            http_method='POST')
        @ndb.transactional
        def create_user_post(self, request):
            # TODO(james7132): Make this validate that the user is a part of the
            # circle and not just make it under the user
            author = User.get_current_user()
            # TODO(james7132): Remove this placeholdder
            post = author.create_post('test')
            post.put()
            return post.to_message()

        @endpoints.method(
            POST_RESOURCE,
            PostMessage,
            path=root + '/{author}/posts/{post_id}',
            http_method='GET')
        def get_user_post(self, request):
            author = root_model_class.get_by_name(request.author)
            post = author.get_post(request.post_id) if author else None
            if not post:
                raise NotFoundException('Post not found.')
            return post.to_message()

        @endpoints.method(
            POST_RESOURCE,
            PostMessage,
            path=root + '/{author}/posts/{post_id}',
            http_method='PUT')
        def update_user_post(self, request):
            author = root_model_class.get_by_name(request.author)
            post = author.get_post(request.post_id) if author else None
            return post.to_message()

        @endpoints.method(
            POST_RESOURCE,
            message_types.VoidMessage,
            path=root + '/{author}/posts/{post_id}',
            http_method='DELETE')
        def delete_user_post(self, request):
            author = root_model_class.get_by_name(request.author)
            post = author.get_post(request.post_id) if author else None
            if post:
                post.key.delete()
            else:
                raise NotFoundException('Post not found.')

    PostsApi.__name__ = root_model_class.__name__ + PostsApi.__name__
    return PostsApi


UserPostsApi = post_api(User, 'users')
CirclePostsApi = post_api(Circle, 'circles')
