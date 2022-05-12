# Register your models here.
from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'category', 'approved', 'created_at')
    readonly_fields = ('created_at', 'post_id')
    date_hierarchy = 'created_at'
    list_filter = ('category',)
    search_fields = ['title', 'author', 'category']
    show_full_result_count = False
