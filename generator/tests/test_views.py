from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from ..models import UrlModel
from ..views import ShortenUrlView, SuccessView, GetOriginalView
from ..utils import generate_a_short_url


class TestGeneratorView(TestCase):

    def test_a_new_url_creating(self):
        response = self.client.post(reverse('generator:shorten-home'), {
            'original_url': 'http://localhost/hey/nananei?foo=bar'
        })
        self.assertRedirects(
            response,
            'http://localhost/hey/nananei?foo=bar',
            fetch_redirect_response=False
        )
        self.assertEqual(UrlModel.objects.count(), 1)

    def test_get_original_view(self):
        entered_url = 'http://localhost/a_url?foo=bar'
        # generate original url first
        url = UrlModel.objects.create(
            original_url=entered_url,
            short_url=generate_a_short_url(size=6)
        )
        response = self.client.get(
            reverse('generator:get-original', args=[url.short_url])
        )
        self.assertRedirects(
            response,
            entered_url,
            fetch_redirect_response=False
        )

    def test_success_page(self):
        # generate original url first
        factory = RequestFactory()
        url = UrlModel.objects.create(
            original_url='http://testserver/hey/nananei?foo=bar',
            short_url=generate_a_short_url(size=6)
        )
        request = factory.get(url.original_url)
        response = SuccessView.as_view()(request)

        self.assertContains(response, url.original_url)
        self.assertContains(response, url.short_url)
