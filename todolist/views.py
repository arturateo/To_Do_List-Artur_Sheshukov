from django.shortcuts import render, get_object_or_404, redirect

from todolist.forms.forms_task import TaskForm
from todolist.models import ToDoList, status_choices


def home(request):
    to_do_list = ToDoList.objects.all()
    data = {'tasks': to_do_list, 'choices': status_choices}
    return render(request, 'index.html', data)


def add_tasks(request):
    if request.method == "GET":
        form = TaskForm()
        datas = {'lists': status_choices}
        return render(request, 'add_tasks.html', {"form": form})
    else:
        date_of_completion = request.POST.get('date_of_completion')
        if not date_of_completion:
            date_of_completion = None
        ToDoList.objects.create(name_task=request.POST.get('name_task'),
                                description=request.POST.get('description'),
                                status=request.POST.get('status'),
                                date_of_completion=date_of_completion)
        return redirect('home')


def detail_task(request, pk):
    to_do_list = get_object_or_404(ToDoList, pk=pk)
    data = {'task': to_do_list, 'choices': status_choices}
    return render(request, 'detail.html', data)


def delete_task(request, pk):
    to_do_list = get_object_or_404(ToDoList, pk=pk)
    to_do_list.delete()
    return redirect('home')


def edit_task(request, pk):
    to_do_list = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'edit.html', {"to_do_list": to_do_list})
