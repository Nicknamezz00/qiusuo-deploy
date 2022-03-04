from django.db import models


class VerifyCode(models.Model):
    phone = models.CharField(max_length=11)
    code = models.CharField(max_length=10)
    add_time = models.DateTimeField(auto_now_add=True)