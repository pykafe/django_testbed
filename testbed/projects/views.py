from django.views.generic.edit import DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Project


class ProjectListView(TemplateView):
    template_name = "projects/project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
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