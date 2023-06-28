from django import forms
from django.forms import widgets

from todolist.models import status_choices


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Название задачи',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=40, required=True, label='Описание задачи', widget=widgets.Textarea(
                                  attrs={"class": "form-control"}))
    status = forms.ChoiceField(required=True, label='Статус', choices=status_choices,
                               widget=forms.Select(attrs={"class": "form-control"}))
    data = forms.DateField(required=False, label='Дата завершения', widget=widgets.DateInput(
                           attrs={"class": "form-control"}))
