from random import choices

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View

from .models import UrlModel


class GeneratorView(View):

    def get(self, request, *args, **kwargs):
        path = request.get_full_path()[1:]  # cut slash char
        try:
            url_model = UrlModel.objects.get(short_url=path)
            return render(request, 'generator/redirect_by_short_url.html', {
                'url_obj': url_model
            })
        except UrlModel.DoesNotExist:
            if not UrlModel.objects.filter(original_url=path).exists():
                url_model = UrlModel.objects.create_url(original_url=path)
            else:
                return HttpResponseBadRequest('This url is already used')
        return render(request, 'generator/url_was_generated.html', {
            'generated_url': url_model
        })
