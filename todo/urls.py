from todo.views import (
    PositionListView,
    PositionDetailView,
    PositionUpdateView,
    PositionDeleteView,

    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
)
from django.urls import path

urlpatterns = [
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/<int:pk>/edit/", PositionUpdateView.as_view(), name="position-edit"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),

    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("task-types/<int:pk>/edit/", TaskTypeUpdateView.as_view(), name="task-type-edit"),
    path("task-types/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
]

app_name = "todo"
