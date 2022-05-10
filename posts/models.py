from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    # Many-to-one.
    author = models.ForeignKey(
        blank=True,
        null=True,
        to='users.UserInfo',
        related_name='post_set',
        default=None,
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        verbose_name=u'作者')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    title = models.TextField(max_length=128, unique=False, verbose_name=u'标题')
    content = models.TextField(
        max_length=1048576,
        blank=True,
        verbose_name=u'内容')
    excerpt = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name=u'引用',
        null=True)
    category = models.ForeignKey(
        verbose_name='学科分类',
        to='subjects.Subject',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='+',
        db_constraint=False)
    status = models.BooleanField(
        default=True,
        verbose_name=u'状态')
    comment = models.ForeignKey(
        verbose_name='评论',
        to='comments.Comment',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='comment_set',
        db_constraint=False)
    likes = models.IntegerField(default=0, verbose_name='点赞数')

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        db_table = 'Post'
        verbose_name = '帖子'
        verbose_name_plural = verbose_name
