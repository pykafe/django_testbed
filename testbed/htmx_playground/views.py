import random
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from render_block import render_block_to_string


class IndexView(TemplateView):
    template_name = 'htmx_playground.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_number'] = str(random.random())[5]
        return context


def RandomNumberView(request):
    context = {'random_number': str(random.random())[5]}
    html = render_block_to_string('htmx_playground.html', 'main', context)
    return HttpResponse(html)
