from django.contrib.auth.models import User
from django.db import models

SEX_CHOICE = ((1, u'男'), (2, u'女'), (3, u'未知'))


class UserInfo(User):
    """
    username, id, first_name, last_name, password derives from AbstractUser.
    """
    age = models.IntegerField(blank=True, null=True, verbose_name=r'年龄')
    created_at = models.DateTimeField(auto_now_add=True)
    qq = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=u'QQ号码'
    )
    avatar = models.URLField(default='avatar/default.png')  # 头像
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        default=None,
        verbose_name=u'手机号码',
    )  # 电话
    gender = models.IntegerField(
        choices=SEX_CHOICE,
        null=True,
        verbose_name=u'性别'
    )  # 性别
    intro = models.CharField(
        null=True,
        blank=True,
        default='你还没有写上个人介绍哦',
        max_length=300,
        verbose_name=u'个人介绍'
    )  # 个人介绍
    post_count = models.IntegerField(default=0)  # 话题数目

    # is_login = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return "User[id=%d, username=%s, password=%s, is_superuser=%s, is_staff=%s]" % (
            self.id, self.username, self.password, self.is_superuser, self.is_staff)

    class Meta:
        ordering = ['id']


class UserTitle(models.Model):
    owner = models.ForeignKey(
        blank=False,
        null=False,
        to=u'users.UserInfo',
        related_name='title_set',
        on_delete=models.CASCADE,
        db_constraint=True,
        verbose_name=u'头衔拥有者'
    )
    title_str = models.TextField(blank=False, verbose_name='用户头衔')


class Subject(models.Model):
    # TODO: ...
    pass
