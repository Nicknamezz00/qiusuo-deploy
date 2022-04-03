from django.db import models


class BaseCategory(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    cate_name = models.CharField(
        '类别',
        unique=True,
        max_length=64,
        null=True,
        blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.cate_name


class Subject(BaseCategory):
    # TODO: This needs to be a tree.
    parent = models.ForeignKey(
        verbose_name='父类别',
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='child')
    # 层级
    level = models.IntegerField('层级', blank=True, null=True)

    class Meta:
        db_table = 'Subject'
        verbose_name = '学科'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cate_name
