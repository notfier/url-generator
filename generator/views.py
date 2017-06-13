import os

from random import choices

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from .models import UrlModel
from .forms import UrlForm
from .utils import generate_a_short_url


class SuccessView(TemplateView):

    template_name = "generator/redirect_by_short_url.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        import ipdb; ipdb.set_trace()
        path = self.request.scheme + '://' + self.request.get_host() + self.request.path
        context['generated_url'] = get_object_or_404(UrlModel, original_url=path)
        return context


class ShortenUrlView(CreateView):
    model = UrlModel
    form_class = UrlForm
    template_name = 'home.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.short_url = generate_a_short_url(size=6)
        self.object = form.save()
        # return super(ShortenUrlView, self).form_valid(form)
        return HttpResponseRedirect(self.object.original_url)


class GetOriginalView(View):

    def get(self, request, short_url):
        url = get_object_or_404(UrlModel, short_url=short_url)
        return HttpResponseRedirect(url.original_url)
