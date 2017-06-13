from django import forms
from django.conf import settings

from .models import UrlModel
from .utils import generate_a_short_url


class UrlForm(forms.ModelForm):

    class Meta:
        model = UrlModel
        fields = ['original_url']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.short_url = generate_a_short_url(size=settings.SHORT_URL_LENGTH)
        if commit:
            instance.save()
        return instance
