from django.urls import path
from .views import ProjectListView, ProjectApproveView

urlpatterns = [
    path('project_list', ProjectListView.as_view(), name='project_list'),
    path('approve_project', ProjectApproveView.as_view(), name='approve_project'),
]
