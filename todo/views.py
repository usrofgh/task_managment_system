from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskSearchForm
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


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    success_url = reverse_lazy("todo:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("todo:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "todo/task_type_list.html"
    context_object_name = "task_type_list"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "todo/task_type_detail.html"
    context_object_name = "task_type_detail"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    manage = TaskType
    template_name = "todo/task_type_form.html"
    context_object_name = "task_type_form"
    success_url = reverse_lazy("todo:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    manage = TaskType
    template_name = "todo/task_type_confirm_delete.html"
    context_object_name = "task_type_confirm_delete"
    success_url = reverse_lazy("todo:task-type-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("todo:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("todo:worker-list")


# class TaskListView(LoginRequiredMixin, generic.ListView):
#     model = Task


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


@login_required
def toggle_join_task(request, pk):
    me = get_user_model().objects.get(id=request.user.id)
    current_task = Task.objects.get(id=pk)
    if (
        me in current_task.assignees.all()
    ):
        current_task.assignees.remove(me)
    else:
        current_task.assignees.add(me)
    return redirect(request.META.get("HTTP_REFERER"))
