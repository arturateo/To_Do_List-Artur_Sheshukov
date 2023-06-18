from django.shortcuts import render
from todolist.models import ToDoList


def home(request):
    to_do_list = ToDoList.objects.all()
    datas = {'lists': to_do_list}
    return render(request, 'index.html', datas)


def add_tasks(request):
    if request.method == "GET":
        print(1)
    else:
        print(2)
