# Generated by Django 3.1 on 2022-03-26 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_function_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('project_approve', 'Can approve projects')]},
        ),
    ]
