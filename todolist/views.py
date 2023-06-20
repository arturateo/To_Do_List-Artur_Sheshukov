from django.shortcuts import render, get_object_or_404, redirect
from todolist.models import ToDoList, status_choices
from django.http import HttpResponseRedirect


def home(request):
    to_do_list = ToDoList.objects.all()
    datas = {'lists': to_do_list, 'choices': status_choices}
    return render(request, 'index.html', datas)


def add_tasks(request):
    if request.method == "GET":
        datas = {'lists': status_choices}
        return render(request, 'add_tasks.html', datas)
    else:
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_of_completion = request.POST.get('date_of_completion')
        if not date_of_completion:
            date_of_completion = None
        ToDoList.objects.create(description=description, status=status, date_of_completion=date_of_completion)
        return HttpResponseRedirect('/')


def delete_task(request, pk):
    todolist_id = request.GET.get(pk=pk)
    todolist = ToDoList.objects.get(pk=todolist_id)
    todolist.delete()
    return redirect(request, 'index.html')
