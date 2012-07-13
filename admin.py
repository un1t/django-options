# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

from .models import Options


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('site', 'site_name',)


admin.site.register(Options, OptionsAdmin)

