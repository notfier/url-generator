from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class UrlModel(models.Model):
    original_url = models.URLField(blank=True, verbose_name=_('original url'))
    short_url = models.SlugField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'))

    def __str__(self):
        return self.original_url
