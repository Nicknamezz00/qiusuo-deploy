from django.db import models
from posts.models import Post as post
from users.models import UserInfo


class UserFavoriteFolder(models.Model):
    user = models.ForeignKey(UserInfo,
                             related_name='favorite_folder_set',
                             null=False,
                             on_delete=models.CASCADE,
                             verbose_name='所关联的用户')

    folder_name = models.CharField(
        max_length=20, null=True, verbose_name='收藏夹')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '收藏夹'
        verbose_name_plural = verbose_name

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

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.folder.folder_name
