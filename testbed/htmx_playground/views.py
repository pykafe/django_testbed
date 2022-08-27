from django.shortcuts import render
from django.views.generic.base import TemplateView

import random


class IndexView(TemplateView):

    def get_template_names(self):
        request = self.request.headers.get('HX-Request') == 'true'
        if request:
            return "partial__random_number.html"
        else:
            return "htmx_playground.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_number'] = str(random.random())[5]
        return context
