from django.contrib import admin
from todolist.models import ToDoList


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_task', 'description', 'status', 'date_of_completion']
    list_display_links = ['id', 'name_task', 'description']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['name_task', 'description', 'status', 'date_of_completion']


admin.site.register(ToDoList, ArticleAdmin)






