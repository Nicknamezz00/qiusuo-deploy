from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'likes',
                    'created_at')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

    actions = ['manual_authenticate']
    search_fields = ('title', 'author__username', 'author__first_name',
                     'author__last_name', 'author__email',
                     'author__qq', 'author__phone')
    show_full_result_count = False
