from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name='index'),
    url(r"^(?P<submission_id>[0-9]+)/$", views.submission_view, name='submission view'),
]
