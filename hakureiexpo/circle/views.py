from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from circle.models import Circle

class CircleDetailView(DetailView):
    model = Circle

class CircleListView(ListView):
    model = Circle
    context_object_name = 'submissions'


class CircleCreate(CreateView):
    model = Circle
    fields = [
        'name',
        'contributors'
    ]


class CircleUpdate(UpdateView):
    model = Circle
    fields = [
        'name',
        'contributors'
    ]


class CircleDelete(DeleteView):
    model = Circle
    success_url = reverse_lazy('circle:list')

