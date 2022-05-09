from django.contrib import admin

from users.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.data.get('password'))
        super().save_model(request, obj, form, change)

    @admin.action(description='执行人工认证')
    def manual_authenticate(self, request, queryset):
        queryset.update(is_manual_authenticated=True)
