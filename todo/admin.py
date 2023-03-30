from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from todo.models import TaskType, Position, Worker, Task


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "position",
                    "email", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {"fields": ("username", "password")}
        ),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email", "position")}
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}
        )
    )

    search_fields = ["username", "first_name", "last_name", "email"]
    ordering = ["username", "last_name", "first_name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    ordering = ["name"]
