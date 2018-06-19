from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel


class TimingMixin():
    last_updated = ndb.DateTimeProperty(auto_now=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class Post(ndb.Model, TimingMixin):
    name = ndb.StringProperty(required=True)
    is_approved = ndb.BooleanProperty(required=True)
    published = ndb.DateTimeProperty(required=False)


class Account(polymodel.PolyModel, TimingMixin):
    name = ndb.StringProperty(required=True)
    display_name = ndb.StringProperty(required=False)
    bio = ndb.TextProperty(required=False)

    def query_posts(self):
        return Post.query(ancestor=self.key).order(-Post.published)

    def create_post(self, name):
        key = ndb.Key(Post, parent=self.key)
        return Post(key=key, name=name, is_approved=False)


class User(Account):
    pass 


class CircleMember(ndb.Model, TimingMixin):
    # TODO(james7132): Add email validation of joining circles
    user_key = ndb.KeyProperty(kind=User, required=True)
    is_owner = ndb.BooleanProperty(required=True)
    role = ndb.StringProperty(required=False)


class Circle(Account):

    def query_members(self):
        return CircleMember.query(ancestor=self.key).order(CircleMember.created_at)

    def create_member(self, user):
        key = ndb.Key(CircleMember, id=user.key.id(), parent=self.key)
        return CircleMember(key=key, is_owner=False)
