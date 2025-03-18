from django.urls import path
from . import views
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("add/", views.add_task, name="add_task"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle_task"),
    path('api/tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path(
        'api/tasks/<int:pk>/',
        TaskRetrieveUpdateDestroyView.as_view(),
        name='task_retrieve_update_destroy',
    ),
]
