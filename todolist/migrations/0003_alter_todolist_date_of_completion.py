# Generated by Django 4.2.2 on 2023-06-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_date_of_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date_of_completion',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]