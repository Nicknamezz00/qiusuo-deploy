from django.contrib import admin
from django.contrib.admin import ModelAdmin

from scratch.models import Scratch


@admin.register(Scratch)
class ScratchAdmin(ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'created_at')
    readonly_fields = ('created_at',)
