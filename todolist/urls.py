from django.urls import path
from todolist.views import home, add_tasks, delete_task, detail_task, edit_task, multiply_delete_task

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_tasks, name='add_task'),
    path('detail/<int:pk>/', detail_task, name='detail_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('delete/multiply/', multiply_delete_task, name='multiply_delete_task')
]
