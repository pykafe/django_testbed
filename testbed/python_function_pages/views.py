from django.http import HttpResponse
from django.views.generic.base import TemplateView

from .libraries.word_count import word_count


class IndexView(TemplateView):
    template_name = "python_function_pages/index.html"


class WordCountView(TemplateView):
    template_name = "python_function_pages/word_count.html"


def count_words(request):
    if "text" in request.POST:
            word_count_result = word_count(request.POST["text"])
    elif "upload_file" in request.FILES:
            word_count_result = word_count(request.FILES["upload_file"].read())
    return HttpResponse(word_count_result)
