from django.db import models


class SubjectCategory_3(models.Model):
    subject = models.CharField(
        unique=True,
        max_length=255,
        null=True,
        verbose_name='三级学科名')
    level = 3

    def __str__(self):
        return self.subject + " " + str(self.level)


class SubjectCategory_2(models.Model):
    subject = models.CharField(
        unique=True,
        max_length=255,
        null=True,
        verbose_name='二级学科名')

    level = 2

    def __str__(self):
        return self.subject + " " + str(self.level)


class SubjectCategory_1(models.Model):
    subject = models.CharField(
        unique=True,
        max_length=255,
        null=True,
        verbose_name='一级学科名')

    level = 1

    def __str__(self):
        return self.subject + " " + str(self.level)


