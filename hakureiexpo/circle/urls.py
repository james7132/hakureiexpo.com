from django.conf.urls import url
from circle.views import *

urlpatterns = [
    url(r"^list$", CircleListView.as_view(), name='list'),
    url(r"^new$", CircleCreate.as_view(), name="create"),
    url(r"^(?P<slug>[a-zA-Z0-9]+)/update$", CircleCreate.as_view(),
        name="update"),
    url(r"^(?P<slug>[a-zA-Z0-9]+)/delete$", CircleDelete.as_view(),
        name="delete"),
    url(r"^(?P<slug>[a-zA-Z0-9]+)$", CircleDetailView.as_view(),
        name="detail"),
]
