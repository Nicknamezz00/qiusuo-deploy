from django.contrib import admin

# Register your models here.
from favorite.models import UserFavorite, UserFavoriteFolder

admin.site.register(UserFavorite)
admin.site.register(UserFavoriteFolder)