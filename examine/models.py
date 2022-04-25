from django.db import models


class TitleExamine(models.Model):
    owner = models.ForeignKey(
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        to='users.UserInfo',
        related_name='title_examined_set',
        verbose_name='拥有者',
    )
    created_time = models.DateTimeField(auto_now=True, verbose_name='申请提交时间')
    title = models.CharField(max_length=100, verbose_name='内容-职称')
    real_name = models.CharField(max_length=100, verbose_name='真实姓名')
    id_card = models.CharField(max_length=100, verbose_name='身份证号', default='')
    school_id_card = models.CharField(
        max_length=100,
        verbose_name='学号/工号',
        null=False,
        blank=False)
    school = models.ForeignKey(
        'informations.School',
        verbose_name='学校',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_constraint=False)
    is_approved = models.BooleanField(default=False, verbose_name='是否已通过审核')
    is_rejected = models.BooleanField(default=False, verbose_name='是否已被拒绝')
    reject_reason = models.CharField(
        max_length=100, verbose_name='拒绝理由', default='')

    def __str__(self):
        return self.real_name + ' ' + self.school.school_name

    class Meta:
        db_table = 'TitleExamine'
        verbose_name = '职称审核'
        verbose_name_plural = verbose_name
