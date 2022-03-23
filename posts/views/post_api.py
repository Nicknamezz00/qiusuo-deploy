from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.filters import PostFilter
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    # 最新的帖子
    queryset = Post.objects.all().order_by('created_at').reverse()
    serializer_class = PostSerializer

    filter_class = PostFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    @action(methods=['POST'], detail=True)
    def thumbs_up(self, request, pk):
        instance = Post.objects.get(id=pk)
        if not instance:
            raise ObjectDoesNotExist()

        instance.likes += 1
        instance.save()

        return Response(data={
            "code": 200,
            "msg": "success",
            "likes": instance.likes,
        }, status=status.HTTP_200_OK)

