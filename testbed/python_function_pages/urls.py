from django.urls import path
from .views import IndexView, ValidSpacingView, WordCountView, ProjectListView

urlpatterns = [
    path('', IndexView.as_view()),
    path('word_count', WordCountView.as_view(), name='word_count'),
    path('valid_spacing', ValidSpacingView.as_view(), name='valid_spacing'),
    path('project_list', ProjectListView.as_view(), name='project_list'),
]
