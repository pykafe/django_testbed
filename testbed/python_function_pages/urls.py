from django.urls import path
from .views import IndexView, ValidSpacingView, WordCountView

urlpatterns = [
    path('', IndexView.as_view()),
    path('word_count', WordCountView.as_view(), name='word_count'),
    path('valid_spacing', ValidSpacingView.as_view(), name='valid_spacing'),
]
