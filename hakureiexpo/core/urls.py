from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^(?P<submission_id>[0-9]+)", views.submission_view, name='submission.view'),
    url(r"^circle/(?P<circle_name>\w+)", views.circle_view, name='circle.view'),
    url(r"^user/(?P<username>\w+)$", views.user_view, name='user.view'),
    url(r"^$", views.index, name='index'),
]
