# -*- coding: utf-8 -*-
from django.contrib import admin
from es.parliament import models

class ESParlamentaryAdmin(admin.ModelAdmin):
    model = models.ESParlamentary
    list_display = ('last_name', 'first_name')

admin.site.register(models.ESParlamentary, ESParlamentaryAdmin)
