from django.db import models


class Subject(models.Model):
    subject = models.CharField(max_length=255, verbose_name='学科名')
    level = models.IntegerField(verbose_name='层级', null=True)

    def __str__(self):
        return self.subject + " " + str(self.level)
