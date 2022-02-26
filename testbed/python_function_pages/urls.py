from django.urls import path
from .views import IndexView, WordCountView, count_words

urlpatterns = [
    path('', IndexView.as_view()),
    path('word_count', WordCountView.as_view(), name='word_count'),
    path('count_words', count_words, name='count_words'),
]
