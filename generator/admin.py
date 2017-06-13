from django.contrib import admin

from .models import UrlModel


@admin.register(UrlModel)
class UrlAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['__str__', 'short_url', 'created_date']
    list_filter = ['created_date']
