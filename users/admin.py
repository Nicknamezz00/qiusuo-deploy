from django.contrib import admin

from users.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'position',
                    'subject', 'school', 'is_manual_authenticated',
                    )
    readonly_fields = ('password', 'date_joined', 'last_login')
    date_hierarchy = 'created_at'
    actions = ['manual_authenticate']
    search_fields = ['username']
    show_full_result_count = False

    # Order matters.
    list_filter = ('is_manual_authenticated',
                   'position',
                   'subject__cate_name',)

    # Order matters.
    fieldsets = (
        (None, {
            'fields': (
                'username', 'password', 'phone', 'email',
                'qq', 'intro', 'age', 'avatar',
                ('first_name', 'last_name'),
                'subject', 'school', 'position',
                'is_manual_authenticated',
                ('date_joined', 'last_login'),
            )
        }),
    )

    @admin.action(description='执行人工认证')
    def manual_authenticate(self, request, queryset):
        queryset.update(is_manual_authenticated=True)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.data.get('password'))
        super().save_model(request, obj, form, change)
