from django.db import models


class VerifyCode(models.Model):
    phone = models.CharField(max_length=11)
    code = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'VerifyCode'
        verbose_name = '验证码'
        verbose_name_plural = verbose_name
