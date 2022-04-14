from django.contrib import admin

# Register your models here.
from feedback.models import Feedback, FeedbackReply

admin.site.register(Feedback)
admin.site.register(FeedbackReply)
