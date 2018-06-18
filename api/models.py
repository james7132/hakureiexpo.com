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
