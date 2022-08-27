from django.shortcuts import render
from django.views.generic.base import TemplateView

import random


class IndexView(TemplateView):
    template_name = "htmx_playground.html"


class RandomNumberView(TemplateView):
    template_name = "partial__random_number.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_number'] = str(random.random())[5]
        return context
