import webapp2
import json
from google.appengine.ext import ndb


class Thing(ndb.Model):
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class Account(Thing):
    name = ndb.StringProperty(required=True)
    display_name = ndb.StringProperty(required=False)
    is_mod = ndb.BooleanProperty(required=True)
    is_circle = ndb.BooleanProperty(required=True)


class CircleMember(ndb.Model):
    user_key = ndb.KeyProperty(kind=Account, required=True)
    is_owner = ndb.BooleanProperty(required=True)
    role = ndb.StringProperty(required=False)


class Post(Thing):
    name = ndb.StringProperty(required=True)
    is_approved = ndb.BooleanProperty(required=True)
    published = ndb.DateTimeProperty(required=False)
    last_updated = ndb.DateTimeProperty(auto_now=True)


def model_to_dict(model, excluded_keys=[]):
    model_dict = model.to_dict()
    for key in excluded_keys:
        model_dict.pop(key, None)
    return model_dict


class RestHandler(webapp2.RequestHandler):

    def dispatch(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers.add_header('Access-Control-Allow-Headers', 'Content-Type')
        webapp2.RequestHandler.dispatch(self)

    def send_json(self, content):
        self.response.headers['Content-Type'] = 'application/json'

        self.response.out.write(json.dumps(content))


class AccountHandler(RestHandler):

    @ndb.transactional
    def get(self, user_name):
        user = ndb.Key(Account, user_name).get()
        if user:
          self.json_response(model_to_dict(user))
        else:
          self.response.set_status(404)

class ListPostsHandler(RestHandler):

    POSTS_PER_PAGE = 20

    def get(self):
        results = Post.query(Post.published !=
                None).order(-Post.published).fetch(self.POSTS_PER_PAGE)
        json_results = [model_to_dict(post) for result in results]
        self.send_json(json_results)

app = webapp2.WSGIApplication([
    ('/api/v1/posts', ListPostsHandler),
    ('/api/v1/user/(\d+)', AccountHandler),
], debug=True)
