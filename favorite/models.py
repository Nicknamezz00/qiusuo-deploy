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

    folder_name = models.CharField(max_length=20, null=True, verbose_name='收藏文件夹名字')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_name


class UserFavorite(models.Model):
    folder = models.ForeignKey(UserFavoriteFolder,
                               related_name='favorite_set',
                               null=False,
                               on_delete=models.CASCADE,
                               verbose_name='所关联的文件夹')

    post = models.ForeignKey(post,
                             related_name='related_favorite',
                             null=False,
                             on_delete=models.CASCADE,
                             verbose_name='收藏所关联的文章')

    def __str__(self):
        return self.folder.folder_name
