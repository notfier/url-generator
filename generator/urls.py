from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^success/(?P<short_url>[A-Za-z0-9]{6})/$', views.SuccessView.as_view(), name='get-success'),
    url(r'^(?P<short_url>[A-Za-z0-9]{6})/$', views.GetOriginalView.as_view(), name='get-original'),
    url(r'^$', views.ShortenUrlView.as_view(), name='shorten-home'),
]
