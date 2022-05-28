from django.views.generic.base import TemplateView

from .libraries.word_count import wc
from .libraries.valid_spacing import valid_spacing


class IndexView(TemplateView):
    template_name = "python_function_pages/index.html"


class WordCountView(TemplateView):
    template_name = "python_function_pages/word_count.html"

    def post(self, request, *args, **kwargs):
        # use request.POST["text"] here in our functions which count words
        # add the result to the request

        if "text" in request.POST:
            self.wc_result = wc(request.POST["text"])
        elif "upload_file" in request.FILES:
            self.wc_result_file = wc(request.FILES["upload_file"].read())

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = getattr(self, 'wc_result', "Submit the form to count words")
        context['file_result'] = getattr(self, 'wc_result_file', "Submit the form to count words")
        return context


class ValidSpacingView(TemplateView):
    template_name = "python_function_pages/valid_spacing.html"
    def post(self, request, *args, **kwargs):
        if "text" in request.POST:
            self.result = valid_spacing(request.POST["text"])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = getattr(self, 'result', "Submit the form to see the valid spacing result")
        return context