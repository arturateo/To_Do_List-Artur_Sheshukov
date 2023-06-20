from django.urls import path
from todolist.views import home, add_tasks, delete_task

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_tasks, name='add_task'),
    path('delete/', delete_task, name='delete_task')
]
