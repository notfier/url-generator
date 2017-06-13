from django.db import models
from django.utils.translation import ugettext as _

from .managers import UrlManager


class UrlModel(models.Model):
    original_url = models.URLField(blank=True, verbose_name=_('original url'))
    short_url = models.SlugField(max_length=10, unique=True, verbose_name=_('short url'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'))

    objects = UrlManager()

    def __str__(self):
        return self.original_url

    def get_absolute_url(self):
        return '/{0}'.format(self.original_url)
