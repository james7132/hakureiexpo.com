import endpoints
from .messages import *
from .exceptions import NotFoundException
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel


class TimingMixin():
    last_updated = ndb.DateTimeProperty(auto_now=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class Post(ndb.Model, TimingMixin):
    name = ndb.StringProperty(required=True)
    is_approved = ndb.BooleanProperty(required=True)
    published = ndb.DateTimeProperty(required=False)
    description = ndb.StringProperty(required=False)

    def to_message(cls, model):
        msg = PostMessage()
        copy_attrs(model, msg, [
            'created_at', 'last_updated', 'name',
            'published', 'description', 'author_id'
        ])
        id = model.key.id()
        return msg

    def to_summary(cls, model):
        msg = PostSummary()
        msg.id = model.key.id()
        copy_attrs(post, msg, ['description'])
        return msg

    @classmethod
    def to_summaries(cls, user, posts):
        msg = PostListMessage()
        msg.author_id = user.key.id()
        msg.posts = [post.to_summary() for post in posts]
        return msg


class Account(polymodel.PolyModel, TimingMixin):
    name = ndb.StringProperty(required=True)
    display_name = ndb.StringProperty(required=False)
    bio = ndb.TextProperty(required=False)

    @property
    def author_id(self):
        # Key format: ('Account', [author_id], 'Post', post_id)
        return self.key.flat()[1]  # Select second element

    @classmethod
    def get_by_name(cls, name, **kwargs):
        return next(cls.query(cls.name == name, **kwargs).fetch(1), None)

    def get_post(self, post_id):
        return ndb.Key(Post, post_id, parent=self.key).get()

    def query_posts(self):
        return Post.query(ancestor=self.key).order(-Post.published)

    def create_post(self, name):
        key = ndb.Key(Post, parent=self.key)
        return Post(key=key, name=name, is_approved=False)


class User(Account):

    email = ndb.StringProperty(required=True)

    @classmethod
    def get_key(cls, user_obj):
        return ndb.Key(cls, user_obj.user_id())

    @classmethod
    def create_user(cls, user_obj, username):
        return cls(
            key=cls.get_key(user_obj),
            name=username,
            display=username,
            email=user_obj.email()
        )

    @classmethod
    def get_user(cls, user_obj):
        return cls.get_by_id(user_obj.user_id())

    @classmethod
    def get_curret_user(cls):
        return cls.get_user(endpoints.get_current_user())

    def to_message(cls, model, include_email=False):
        msg = UserMessage()
        copy_attrs(model, msg, [
            'created_at', 'last_updated', 'display_name', 'name', 'bio'
        ])
        msg.id = model.key.id()
        if include_email and hasattr(msg, 'email'):
            msg.email = model.email
        return msg


class CircleMember(ndb.Model, TimingMixin):
    user = ndb.KeyProperty(kind=User, required=True)
    is_owner = ndb.BooleanProperty(required=True)
    role = ndb.StringProperty(required=False)
    is_email_validated = ndb.BooleanProperty(required=True)

    @classmethod
    def create_key(cls, circle, user):
        return ndb.Key(cls, id=user.key.id(), parent=circle.key)

    def to_message(self):
        msg = CircleMemberMessage()
        copy_attrs(self, msg, ['is_owner', 'role'])
        msg.user_id = model.user.id()
        return msg

    @classmethod
    def to_list_message(cls, members):
        msg = CircleMemberListResponse()
        msg.circle_id = circle.key.id()
        msg.members = [member.to_list() for member in members]
        return msg


class Circle(Account):

    def get_member(self, user):
        return CircleMember.create_key(self, user).get()

    def query_members(self):
        return CircleMember.query(ancestor=self.key).order(CircleMember.created_at)

    def create_member(self, user):
        key = CircleMember.create_key(self, user)
        return CircleMember(key=key, is_owner=False)

    def to_message(self):
        msg = CircleMessage()
        copy_attrs(self, msg, [
            'created_at', 'last_updated', 'display_name', 'name', 'bio', 'email'
        ])
        msg.id = model.key.id()
        return msg
