from django import forms
from django.conf import settings

from .models import UrlModel
from .utils import generate_a_short_url


class UrlForm(forms.ModelForm):

    class Meta:
        model = UrlModel
        fields = ['original_url']
