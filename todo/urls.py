from todo.views import (
    PositionListView,
    PositionDetailView,
    PositionUpdateView,
    PositionDeleteView,
)
from django.urls import path

urlpatterns = [
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/<int:pk>/edit/", PositionUpdateView.as_view(), name="position-edit"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]

app_name = "todo"
