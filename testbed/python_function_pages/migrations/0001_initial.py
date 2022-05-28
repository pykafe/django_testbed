# Generated by Django 3.1 on 2022-03-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the catlapa project', max_length=64, unique=True)),
                ('description', models.TextField(blank=True, help_text='Shart description of the project', null=True)),
                ('start_date', models.DateField(blank=True, help_text='The starting date of the project', null=True)),
                ('end_date', models.DateField(blank=True, help_text='The end date of the project', null=True)),
            ],
        ),
    ]
