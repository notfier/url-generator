from django.test import TestCase

from ..models import UrlModel


class TestUrlModelMethods(TestCase):

    def test_str_method(self):
        url = UrlModel.objects.create_url(original_url='/a/test/?foo=bar')
        self.assertEqual(str(url), url.original_url)

    def test_get_absolute_url(self):
        url = UrlModel.objects.create_url(original_url='/a/test/?foo=bar')
        self.assertEqual(url.get_absolute_url(), ''.join(['/', url.original_url]))