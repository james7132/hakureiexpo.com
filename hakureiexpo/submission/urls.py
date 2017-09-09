from django.conf.urls import url
from submission.views import *

urlpatterns = [
    url(r"^list$", SubmissionListView.as_view(), name='list'),
    url(r"^new$", SubmissionCreate.as_view(), name="create"),
    url(r"^(?P<slug>[a-zA-Z0-9]+)/update$", SubmissionCreate.as_view(),
        name="update"),
    url(r"^(?P<slug>[a-zA-Z0-9]+)/delete$", SubmissionDelete.as_view(),
        name="delete"),
    url(r"^(?P<slug>[a-zA-Z0-9]+)$", SubmissionDetailView.as_view(),
        name="detail"),
]
