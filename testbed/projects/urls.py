from django.urls import path
from .views import ProjectListView, ProjectApproveView, ProjectRejectView, ProjectDeleteView

urlpatterns = [
    path('project_list', ProjectListView.as_view(), name='project_list'),
    path('approve_project/<int:pk>/', ProjectApproveView.as_view(), name='approve_project'),
    path('reject_project/<int:pk>/', ProjectRejectView.as_view(), name='reject_project'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete_project'),
]
