from django.urls import path
from .views import IndexView, RandomNumberView

urlpatterns = [
    path('', IndexView.as_view()),
    path('random', RandomNumberView.as_view()),
]
