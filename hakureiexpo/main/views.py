from django.shortcuts import get_object_or_404, render

from .models import Submission

# Create your views here.


def index(request):
    submissions = Submission.objects.order_by('-publish_date')[:5]
    context = { 'submission_list': submissions }
    return render(request, 'index.html', context)


def submission_view(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    context = { 'submission': submission }
    return render(request, 'detail.html', context)

