from django.urls import path

from .views import (
    TagCreateView,
    TagListView,
    TagDetailView,
    TagDeleteView,
    TagUpdateView,
    TaskCreateView,
    TaskListView,
    TaskDeleteView,
    TaskUpdateView,
    TaskToggleView,
)

urlpatterns = [

    path("tags/create", TagCreateView.as_view(), name="tag-form"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-confirm-delete"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-form"),
    path("tasks/create", TaskCreateView.as_view(), name="task-form"),
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-confirm-delete"),
    # path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-form"),
    path('task-toggle/<int:pk>/', TaskToggleView.as_view(), name='task-toggle'),

]

app_name = "todolist"
