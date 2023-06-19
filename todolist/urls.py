from django.urls import path
from todolist.views import home, add_tasks, delete_task

urlpatterns = [
    path('', home),
    path('add/', add_tasks),
    path('delete/', delete_task)
]
