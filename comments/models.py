from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(
        to='users.UserInfo',
        on_delete=models.DO_NOTHING,
        related_name='comment_set',
        verbose_name=u'评论者',
        db_constraint=False
    )

    post_id = models.BigIntegerField(verbose_name=u'帖子id')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    content = models.TextField(verbose_name=u'内容')
    approved = models.BigIntegerField(default=0, verbose_name=u'赞成')
    category = models.CharField(max_length=20, null=True, verbose_name=u'种类')

    # owner = models.ManyToManyField(User, related_name='comment_owner_set', blank=True)

    def __str__(self):
        return self.author.username
