# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import FlatPage


class FlatPageAdmin(admin.ModelAdmin):
    list_display_over = ('url', 'title', 'template_name')
    list_display = list_display_over
    list_display_links = list_display_over
    search_fields = ('url', 'title')


admin.site.register(FlatPage, FlatPageAdmin)
