from django.db import models


class Scratch(models.Model):
    user = models.ForeignKey(
        verbose_name='用户',
        to='users.UserInfo',
        db_constraint=False,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='scratch_set'
    )
    content = models.TextField('内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __str__(self):
        return "user: {0}".format(self.user.username)

    class Meta:
        db_table = 'Scratch'
        verbose_name = '暂存箱'
        verbose_name_plural = verbose_name
