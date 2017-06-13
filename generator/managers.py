from django.db import models
from django.conf import settings

from .utils import generate_a_short_url


class UrlManager(models.Manager):
    """
    Create url with auto generated short url.
    """
    def create_url(self, original_url):
        url = self.create(
            original_url=original_url,
            short_url=generate_a_short_url(size=settings.SHORT_URL_LENGTH)
        )
        return url
