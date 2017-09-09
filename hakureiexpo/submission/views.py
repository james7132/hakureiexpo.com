from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from submission.models import Submission

class SubmissionDetailView(DetailView):
    model = Submission

class SubmissionListView(ListView):
    model = Submission
    context_object_name = 'submissions'


class SubmissionCreate(CreateView):
    model = Submission
    fields = [
        'title',
        'description',
        'image',
        'external_link',
        'circle',
        'type',
        'subtype',
        'is_public'
    ]


class SubmissionUpdate(UpdateView):
    model = Submission
    fields = [
        'title',
        'description',
        'image',
        'external_link',
        'circle',
        'type',
        'subtype',
        'is_public'
    ]


class SubmissionDelete(DeleteView):
    model = Submission
    success_url = reverse_lazy('submission:list')
