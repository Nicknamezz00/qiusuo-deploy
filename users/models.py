from django.contrib import admin
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
        verbose_name=u'QQ号码')
    avatar = models.URLField('头像', default=(
        'https://qiusuo-1310314982.cos.ap-guangzhou.myqcloud.com/media/avatar/825ed0c3b35e053013344ee5ade03458.png'
    ))
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        default=None,
        verbose_name=u'手机号码')  # 电话
    gender = models.IntegerField(
        choices=SEX_CHOICE,
        null=True,
        blank=True,
        verbose_name=u'性别')  # 性别
    intro = models.CharField(
        null=True,
        blank=True,
        default='你还没有写上个人介绍哦',
        max_length=300,
        verbose_name=u'个人介绍')  # 个人介绍
    subject = models.ForeignKey(
        verbose_name='专业',
        to='subjects.Subject',
        null=True,
        blank=True,
        related_name='subject_set',
        on_delete=models.DO_NOTHING,
        db_constraint=False)
    school = models.ForeignKey(
        verbose_name='学校',
        to='informations.School',
        null=True,
        blank=True,
        related_name='school',
        on_delete=models.DO_NOTHING,
        db_constraint=False)
    position = models.CharField('职位', max_length=64, null=True, blank=True)

    area1 = models.ForeignKey(
        verbose_name='领域1',
        to='subjects.Subject',
        to_field='cate_name',
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_constraint=False)
    area2 = models.ForeignKey(
        verbose_name='领域2',
        to='subjects.Subject',
        to_field='cate_name',
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_constraint=False)
    area3 = models.ForeignKey(
        verbose_name='领域3',
        to='subjects.Subject',
        to_field='cate_name',
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_constraint=False)

    # permissions:
    is_manual_authenticated = models.BooleanField(
        '人工认证', default=False, help_text=(
            'Designates whether this user should be treated as manual authenticated. '
            'Unselect this instead of deleting accounts.'))

    def __str__(self):
        return self.username

    def __repr__(self):
        return "User[id=%d, username=%s, password=%s, is_superuser=%s, is_staff=%s]" % (
            self.id, self.username, self.password, self.is_superuser, self.is_staff)

    @property
    @admin.display(ordering='last_name', description='姓名', )
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['id']
        db_table = 'UserInfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class UserTitle(models.Model):
    owner = models.ForeignKey(
        blank=False,
        null=False,
        to='users.UserInfo',
        related_name='title_set',
        on_delete=models.CASCADE,
        db_constraint=True,
        verbose_name=u'头衔拥有者')
    title_str = models.TextField(
        max_length=20,
        blank=False,
        verbose_name='用户头衔')

    def __str__(self):
        return self.owner.username + ' ' + self.title_str

    class Meta:
        db_table = 'UserTitle'
        verbose_name = '用户头衔'
        verbose_name_plural = verbose_name
