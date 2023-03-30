from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Worker, Task, Position, TaskType


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


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "todo/task_type_list.html"
    context_object_name = "task_type_list"


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    template_name = "todo/task_type_detail.html"
    context_object_name = "task_type_detail"


class TaskTypeUpdateView(generic.UpdateView):
    manage = TaskType
    template_name = "todo/task_type_form.html"
    context_object_name = "task_type_form"
    success_url = reverse_lazy("catalog:task-type-list")


class TaskTypeDeleteView(generic.DeleteView):
    manage = TaskType
    template_name = "todo/task_type_confirm_delete.html"
    context_object_name = "task_type_confirm_delete"
    success_url = reverse_lazy("catalog:task-type-list")


class WorkerListView(generic.ListView):
    model = Worker


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("catalog:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("catalog:worker-list")
