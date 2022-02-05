from django.urls import path
from .views import IndexView, WordCountView

urlpatterns = [
    path('', IndexView.as_view()),
    path('word_count', WordCountView.as_view(), name='word_count'),
]
