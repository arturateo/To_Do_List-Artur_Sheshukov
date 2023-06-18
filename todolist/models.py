from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class ToDoList(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание задачи')
    status = models.CharField(max_length=40, null=False, blank=False, default='new', verbose_name='Статус',
                              choices=status_choices)
    date_of_completion = models.DateField(null=True, blank=True, default='none', verbose_name='Дата выполнения')

    def __str__(self):
        return f'{self.pk} {self.description}, {self.status}, {self.date_of_completion}'

    class Meta:
        db_table = "to_do_list"
        verbose_name = "Список задач"
        verbose_name_plural = "Список задач"
