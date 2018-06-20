import endpoints

# Add Firebase Auth as an auth provider
firebase_auth = endpoints.Issuer(
    'https://securetoken.google.com/hakurei-expo',
    'https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com')

api_collection = endpoints.api(
    name='hakurei-expo',
    version='v1',
    issuers={'firebase': firebase_auth})

from .users import UsersApi
from .posts import UserPostsApi, CirclePostsApi
from .circles import CirclesApi
