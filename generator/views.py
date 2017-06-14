from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse

from .models import UrlModel
from .forms import UrlForm
from .utils import generate_a_short_url


class SuccessView(TemplateView):

    template_name = "generator/redirect_by_short_url.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['url_obj'] = get_object_or_404(
            UrlModel,
            short_url=self.kwargs.get('short_url')
        )
        return context


class ShortenUrlView(CreateView):
    model = UrlModel
    form_class = UrlForm
    template_name = 'home.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse('generator:get-success', args=[self.object.short_url]))


class GetOriginalView(View):

    def get(self, request, short_url):
        url = get_object_or_404(UrlModel, short_url=short_url)
        return HttpResponseRedirect(url.original_url)
