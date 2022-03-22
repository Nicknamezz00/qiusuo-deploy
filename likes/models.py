from django.db import models
from posts.models import Post as post
from users.models import UserInfo


# Create your models here.
class UserLike(models.Model):
    Post = models.ForeignKey(post, related_name='id', null=False, on_delete=models.CASCADE)
    User = models.ForeignKey(UserInfo, related_name='id', null=False, on_delete=models.CASCADE)
