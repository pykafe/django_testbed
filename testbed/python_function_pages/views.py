from urllib import request
from django.views.generic.base import TemplateView

from .libraries.word_count import wc

class IndexView(TemplateView):
    template_name = "python_function_pages/index.html"


class WordCountView(TemplateView):
    template_name = "python_function_pages/word_count.html"

    def post(self, request, *args, **kwargs):
        # use request.POST["text"] here in our functions which count words
        # add the result to the request

        self.wc_result = wc(request.POST["text"])

        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = getattr(self, 'wc_result', "Submit the form to count words")
        return context