from django.urls import path
from todolist.views import home

urlpatterns = [
    path('', home),
]
