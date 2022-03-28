from django.db import models


class BaseCategory(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subject(BaseCategory):
    # TODO: This needs to be a tree.
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='child')
    # 层级
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Subject'
