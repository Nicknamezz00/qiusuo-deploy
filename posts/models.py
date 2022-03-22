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
        verbose_name=u'作者'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    title = models.TextField(unique=True, verbose_name=u'标题')
    content = models.TextField(blank=True, verbose_name=u'内容')
    excerpt = models.TextField(blank=True, verbose_name=u'引用', null=True)
    category = models.CharField(blank=True, max_length=20, verbose_name=u'种类', null=True)
    status = models.CharField(
        max_length=20,
        default='active',
        verbose_name=u'状态'
    )
    parent = models.BigIntegerField(default=-1, verbose_name=u'父节点')
    comment_count = models.BigIntegerField(default=0, verbose_name=u'评论数')
    likes = models.IntegerField(default=0, verbose_name='点赞数')


    def __str__(self):
        return self.author.id

    def __repr__(self):
        return self.author.id
