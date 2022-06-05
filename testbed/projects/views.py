from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Project


class ProjectListView(TemplateView):
    template_name = "projects/project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['organisation_name'] = 'Catalpa'
        return context


class ProjectApprovalStatusBaseView(TemplateView):
    """Base class for views that update a project apporval status"""
    template_name = "projects/partials/project_approval.html"
    new_approval_status = Project.APPROVAL_APPROVED
    
    def post(self, request, pk):
        # this might be better, as only one sql statement
        # Project.objects.filter(pk=pk).update(approval_status=Project.APPROVAL_APPROVED)
        project = Project.objects.get(pk=pk)
        project.approval_status = self.new_approval_status
        project.save()
        self.project = project
        return super().get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context


class ProjectRejectView(ProjectApprovalStatusBaseView):
    new_approval_status = Project.APPROVAL_REJECTED


class ProjectApproveView(ProjectApprovalStatusBaseView):
    new_approval_status = Project.APPROVAL_APPROVED


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')
    template_name = "projects/partials/project_confirm_delete.html"


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('project_list')
    template_name = "projects/partials/create.html"

    def form_valid(self, form):
        redirect = super().form_valid(form)
        # not redirect, but render the project row, with the updated project
        if "add_another" in self.request.GET:
            template = "projects/partials/create.html" 
            form_class=self.get_form_class()
            context = dict(
                form=form_class()
            )
        else:
            template = "projects/partials/project_list.html" 
            context = dict(
                projects=Project.objects.all()
            )
        return render(
            self.request, 
            template, 
            context
        )


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('project_list')
    template_name = "projects/partials/update.html"
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        redirect = super().form_valid(form)
        # not redirect, but render the project row, with the updated project
        template = "projects/partials/project_list.html" 
        context = dict(
            projects=Project.objects.all()
        )
        return render(
            self.request, 
            template, 
            context
        )
