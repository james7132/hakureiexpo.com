import endpoints

api_collection = endpoints.api(name='hakurei-expo', version='v1')

from .users import UsersApi
