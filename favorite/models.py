from django.db import models
from posts.models import Post as post
from users.models import UserInfo


# Create your models here.
class UserFavoriteFolder(models.Model):
    user = models.ForeignKey(UserInfo,
                             related_name='favorite_folder_set',
                             null=False,
                             on_delete=models.CASCADE,
                             verbose_name='所关联的用户')

    name = models.CharField(max_length=20, null=False, verbose_name='文件夹名字')


class UserFavorite(models.Model):
    folder = models.ForeignKey(UserFavoriteFolder,
                               related_name='favorite_set',
                               null=False,
                               on_delete=models.CASCADE,
                               verbose_name='所关联的文件夹')

    post = models.ForeignKey(post, related_name='+', null=False, on_delete=models.CASCADE, verbose_name='所关联的文章')
