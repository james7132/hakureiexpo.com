from protorpc import message_types, messages, remote


class CircleMessage(messages.Message):
    created_at = message_types.DateTimeField(1, required=True)
    last_updated = message_types.DateTimeField(2, required=True)
    id = message_types.DateTimeField(3, required=True)
    name = messages.StringField(4, required=True)
    display_name = messages.StringField(5, required=False)
    bio = messages.StringField(6, required=False)
    email = messages.StringField(7, required=False)


class CircleMemberMessage(messages.Message):
    user_id = messages.StringField(1)
    is_owner = messages.BooleanField(2)
    role = messages.StringField(3)


class CircleMemberListMessage(messages.Message):
    circle_id = messages.StringField(1)
    members = messages.MessageField(CircleMemberMessage, 2, repeated=True)


class PostMessage(messages.Message):
    created_at = message_types.DateTimeField(1, required=True)
    last_updated = message_types.DateTimeField(2, required=True)
    author_id = messages.StringField(4, required=True)
    id = message_types.DateTimeField(5, required=True)
    published = message_types.DateTimeField(6, required=False)
    description = messages.StringField(7, required=False)


class PostSummary(messages.Message):
    id = messages.StringField(1)
    description = messages.StringField(2)


class PostListMessage(messages.Message):
    author_id = messages.StringField(1)
    posts = messages.MessageField(PostSummary, 2, repeated=True)


class UserMessage(messages.Message):
    created_at = message_types.DateTimeField(1, required=True)
    last_updated = message_types.DateTimeField(2, required=True)
    id = message_types.DateTimeField(3, required=True)
    name = messages.StringField(4, required=True)
    display_name = messages.StringField(5, required=False)
    bio = messages.StringField(6, required=False)
    email = messages.StringField(7, required=False)
