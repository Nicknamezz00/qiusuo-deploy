from django.db import models

from users.models import UserInfo


# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(UserInfo,
                             related_name="feedback_set",
                             on_delete=models.DO_NOTHING,
                             verbose_name="提供关联的用户"
                             )

    title = models.TextField(max_length=128,
                             null=False,
                             blank=False,
                             verbose_name="反馈标题"
                             )

    content = models.TextField(max_length=65535,
                               null=False,
                               blank=False,
                               verbose_name="反馈内容"
                               )

    is_processing = models.BooleanField(default=False,
                                        verbose_name="是否正在处理用户反馈")

    is_finished = models.BooleanField(default=False,
                                      verbose_name="是否完成用户反馈内容")

    created_at = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feedback'
        verbose_name = '用户反馈'
        verbose_name_plural = verbose_name


class FeedbackReply(models.Model):
    owner = models.ForeignKey(UserInfo,
                              on_delete=models.DO_NOTHING,
                              verbose_name="该反馈评论发起者"
                              )

    related_feedback = models.ForeignKey(Feedback,
                                         related_name="reply_set",
                                         on_delete=models.CASCADE,
                                         verbose_name="相关联的反馈"
                                         )

    content = models.TextField(max_length=1024,
                               null=False,
                               blank=False,
                               verbose_name="评论内容"
                               )

    created_at = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback_reply'
        verbose_name = '反馈回复'
        verbose_name_plural = verbose_name
