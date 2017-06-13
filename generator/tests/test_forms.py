from django.test import TestCase
from django.conf import settings

from ..forms import UrlForm
from ..models import UrlModel


class TestUrlForm(TestCase):

    def test_correct_saving(self):
        form = UrlForm({'original_url': 'http://testserver.com/hey/nananei?foo=bar'})
        if form.is_valid():
            form.save()
        self.assertEqual(len(form.instance.short_url), settings.SHORT_URL_LENGTH)
        self.assertEqual(form.instance, UrlModel.objects.first())
