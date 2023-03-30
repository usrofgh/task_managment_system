from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Worker, Task, Position


def index(request):
    worker_count = Worker.objects.count()
    to_do_count = Task.objects.filter(completing_step=0).count()
    doing_count = Task.objects.filter(completing_step=1).count()
    done_count = Task.objects.filter(completing_step=2).count()

    context = {
        "worker_count": worker_count,
        "to_do_count": to_do_count,
        "doing_count": doing_count,
        "done_count": done_count,
    }
    return render(request, "todo/index.html", context=context)


class PositionListView(generic.ListView):
    model = Position


class PositionDetailView(generic.DetailView):
    model = Position


class PositionUpdateView(generic.UpdateView):
    model = Position
    success_url = reverse_lazy("catalog:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("catalog:position-list")
