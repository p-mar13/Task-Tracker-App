# Generated by Django 4.2.2 on 2024-02-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_todolist_todotask_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='status',
            field=models.CharField(max_length=12),
        ),
    ]
