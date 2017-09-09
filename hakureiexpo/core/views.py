import urllib

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from circle.models import Circle
from submission.models import Submission


def index(request):
    submissions = Submission.objects.order_by('-publish_date')[:5]
    circles = Circle.objects.all()[:5]
    context = {
        'submission_list': submissions,
        'circles': circles,
    }
    return render(request, 'index.html', context)


def user_view(request, username):
    user = get_object_or_404(User, username=urllib.unquote(username))
    context = {'submission': user}
    return render(request, 'user/view.html', context)


def circle_view(request, circle_name):
    submission = get_object_or_404(Circle, name=circle_name)
    context = {'submission': submission}
    return render(request, 'circle/view.html', context)


def submission_view(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    context = {'submission': submission}
    return render(request, 'submission/view.html', context)
