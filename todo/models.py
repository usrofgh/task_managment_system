from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        default_related_name = "task_types"

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        default_related_name = "positions"

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE, null=True)

    class Meta:
        default_related_name = "workers"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    PRIORITIES = (
        ("L", "🟢"),
        ("M", "🟡"),
        ("H", "🔴"),
    )

    TASK_PROGRESS = (
        ("0", "To Do"),
        ("1", "Doing"),
        ("2", "Done")
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    completing_step = models.CharField(max_length=1, choices=TASK_PROGRESS)
    priority = models.CharField(max_length=1, choices=PRIORITIES)

    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to=Worker)

    class Meta:
        default_related_name = "tasks"

    def __str__(self) -> str:
        return self.name
