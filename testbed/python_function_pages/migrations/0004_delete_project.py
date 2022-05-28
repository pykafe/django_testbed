# Generated by Django 3.1 on 2022-04-02 00:54

from django.db import migrations

def forwards_func(apps, schema_editor):
    OldProject = apps.get_model("python_function_pages", "Project")
    NewProject = apps.get_model("projects", "Project")
    db_alias = schema_editor.connection.alias
    for op in OldProject.objects.using(db_alias).all():
        NewProject.objects.using(db_alias).get_or_create(
            name=op.name,
            description=op.description,
            start_date=op.start_date,
            end_date=op.end_date,
        )
def backwards_func(apps, schema_editor):
    OldProject = apps.get_model("python_function_pages", "Project")
    NewProject = apps.get_model("projects", "Project")
    db_alias = schema_editor.connection.alias
    for op in NewProject.objects.using(db_alias).all():
        OldProject.objects.using(db_alias).get_or_create(
            name=op.name,
            description=op.description,
            start_date=op.start_date,
            end_date=op.end_date,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('python_function_pages', '0003_alter_project_options'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            forwards_func,
            backwards_func,
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
