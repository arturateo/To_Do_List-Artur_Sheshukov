from django.urls import path
from todolist.views import home, add_tasks

urlpatterns = [
    path('', home),
    path('add/', add_tasks),
]
