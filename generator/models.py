from django.db import models
from django.utils.translation import ugettext as _

from .utils import generate_a_short_url


class UrlManager(models.Manager):
    """
    Create url with auto generated short url.
    """
    def create_url(self, original_url):
        url = self.create(
            original_url=original_url,
            short_url=generate_a_short_url(size=6)
        )
        return url


class UrlModel(models.Model):
    original_url = models.URLField(blank=True, verbose_name=_('original url'))
    short_url = models.SlugField(max_length=10, unique=True, verbose_name=_('short url'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'))

    objects = UrlManager()

    def __str__(self):
        return self.original_url

    def get_absolute_url(self):
        return '/{0}'.format(self.original_url)
