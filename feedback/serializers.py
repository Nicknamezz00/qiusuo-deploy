from rest_framework import serializers

from feedback.models import Feedback, FeedbackReply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackReply
        fields = ['owner', 'content', 'created_at']


class FeedbackSerializer(serializers.ModelSerializer):
    reply_set = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Feedback
        fields = [
            'user',
            'title',
            'content',
            'is_processing',
            'reply_set',
            'is_finished']
