from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from feedback.models import Feedback, FeedbackReply
from feedback.serializers import FeedbackSerializer, ReplySerializer
from feedback.filter import FeedbackFilter, FeedbackReplyFilter


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_class = FeedbackFilter


class FeedbackReplyViewSet(ModelViewSet):
    queryset = FeedbackReply.objects.all().order_by('-created_at')
    serializer_class = ReplySerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_class = FeedbackReplyFilter
