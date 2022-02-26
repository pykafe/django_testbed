from django.views.generic.base import TemplateView

from .libraries.word_count import word_count


class IndexView(TemplateView):
    template_name = "python_function_pages/index.html"


class WordCountView(TemplateView):
    template_name = "python_function_pages/word_count.html"

    def post(self, request, *args, **kwargs):
        # use request.POST["text"] here in our functions which count words
        # add the result to the request

        if "text" in request.POST:
            self.word_count_result = word_count(request.POST["text"])
        elif "upload_file" in request.FILES:
            self.word_count_result_file = word_count(request.FILES["upload_file"].read())

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = getattr(self, 'word_count_result', "Submit the form to count words")
        context['file_result'] = getattr(self, 'word_count_result_file', "Submit the form to count words")
        return context
