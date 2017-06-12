from random import choices

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View

from .models import UrlModel
from .utils import generate_a_short_url


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
                url_model = UrlModel.objects.create(
                    original_url=path,
                    short_url=generate_a_short_url(size=6)
                )
            else:
                return HttpResponseBadRequest('This url is already used')
        return render(request, 'generator/url_was_generated.html', {
            'generated_url': url_model
        })
