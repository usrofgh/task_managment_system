from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todo.models import Worker, Task


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
