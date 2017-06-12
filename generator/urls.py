from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^[A-Za-z0-9+?/=_-]+', views.GeneratorView.as_view(), name='generator'),
    url(r'^', TemplateView.as_view(template_name='home.html'), name='home'),
]
