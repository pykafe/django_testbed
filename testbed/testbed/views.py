from urllib import request
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

class IndexView(TemplateView):
    template_name = "testbed/index.html"

class HtmxLogin(LoginView):
    template_name = "registration/htmx/login.html"
    def form_valid(self, form):
        old_redirect = super().form_valid(form)
        response = render(
            self.request,
            "testbed/user.html",
        )
        response['HX-Redirect'] = self.request.headers['Hx-Current-Url']
        return response
