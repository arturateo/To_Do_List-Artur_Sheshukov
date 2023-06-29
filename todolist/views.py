from django.shortcuts import render, get_object_or_404, redirect

from todolist.forms.forms_task import TaskForm, TaskMultyDelete
from todolist.models import ToDoList, status_choices


def home(request):
    to_do_list = ToDoList.objects.all()
    data = {'tasks': to_do_list, 'choices': status_choices}
    return render(request, 'index.html', data)


def add_tasks(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'add_tasks.html', {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            date_of_completion = form.cleaned_data['date_of_completion']
            if not date_of_completion:
                date_of_completion = None
            todolist = ToDoList.objects.create(
                name_task=form.cleaned_data['name_task'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                date_of_completion=date_of_completion)
            return redirect('detail_task', pk=todolist.pk)
        else:
            return render(request, 'add_tasks.html', {'form': form})


def detail_task(request, pk):
    to_do_list = get_object_or_404(ToDoList, pk=pk)
    data = {'task': to_do_list, 'choices': status_choices}
    return render(request, 'detail_task.html', data)


def delete_task(request, pk):
    to_do_list = get_object_or_404(ToDoList, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_task.html', {"to_do_list": to_do_list})
    else:
        button = request.POST.get("delete")
        if button:
            to_do_list.delete()
        return redirect('home')


def edit_task(request, pk):
    todolist = get_object_or_404(ToDoList, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'name_task': todolist.name_task,
            'description': todolist.description,
            'status': todolist.status,
            'date_of_completion': todolist.date_of_completion,
        })
        return render(request, 'edit_task.html', {'form': form, 'todolist': todolist})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            date_of_completion = form.cleaned_data['date_of_completion']
            if not date_of_completion:
                date_of_completion = None
            todolist.name_task = form.cleaned_data['name_task']
            todolist.description = form.cleaned_data['description']
            todolist.status = form.cleaned_data['status']
            todolist.date_of_completion = date_of_completion
            todolist.save()
            return redirect('detail_task', pk=todolist.pk)
        else:
            return render(request, 'edit_task.html', {'form': form, 'todolist': todolist})


def multiply_delete_task(request, *args, **kwargs):
    check_list = request.POST.getlist('check')
    for pk in check_list:
        task = get_object_or_404(ToDoList, pk=pk)
        task.delete()
    return redirect('home')
