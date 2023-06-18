from django.contrib import admin
from todolist.models import ToDoList


admin.site.register(ToDoList)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_of_completion']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'date_of_completion']



