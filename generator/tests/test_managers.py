from django.test import TestCase
from django.conf import settings

from ..managers import UrlManager
from ..models import UrlModel


class TestUrlManager(TestCase):

    def test_correct_creation(self):
        url = UrlModel.objects.create_url(original_url='a_dandelion_wine/?answer=yes')
        self.assertTrue(url.short_url)
        self.assertEqual(len(url.short_url), settings.SHORT_URL_LENGTH)
        self.assertIsInstance(UrlModel.objects, UrlManager)