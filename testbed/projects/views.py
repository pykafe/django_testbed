from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Project


class ProjectListView(TemplateView):
    template_name = "projects/project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class ProjectApproveView(TemplateView):
    template_name = "projects/project_approval_fragment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context
