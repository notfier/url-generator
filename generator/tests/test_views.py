from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from ..models import UrlModel
from ..views import GeneratorView
from ..utils import generate_a_short_url


class TestGeneratorView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_a_new_url_creating(self):
        request = self.factory.get(reverse('generator:generator'))
        response = GeneratorView.as_view()(request)
        self.assertContains(response, reverse('generator:generator')[1:])
        self.assertEqual(UrlModel.objects.count(), 1)

    def test_get_an_old_url(self):
        entered_url = '/a_url?foo=bar'
        # generate original url first
        url = UrlModel.objects.create(
            original_url=entered_url[1:],
            short_url=generate_a_short_url(size=6)
        )
        request = self.factory.get(entered_url)
        response = GeneratorView.as_view()(request)

        self.assertContains(response, 'This url is already used', status_code=400)

    def test_aka_redirect(self):
        # generate original url first
        url = UrlModel.objects.create(
            original_url='atata',
            short_url=generate_a_short_url(size=6)
        )
        request = self.factory.get(url.short_url)
        response = GeneratorView.as_view()(request)

        self.assertContains(response, url.original_url)
        self.assertContains(response, url.short_url)
