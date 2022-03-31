from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.filters import PostFilter
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    # 最新的帖子
    queryset = Post.objects.all().order_by('created_at').reverse()
    serializer_class = PostSerializer

    # authentication_classes = [JSONWebTokenAuthentication]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_class = PostFilter

    ordering_fields = ['created_at', 'likes']
    search_fields = ['=author__username', 'category', 'title']

    @action(methods=['POST'], detail=True)
    def thumbs_up(self, request, pk):
        instance = Post.objects.get(id=pk)
        if not instance:
            raise ObjectDoesNotExist()

        instance.likes += 1
        instance.save()

        return Response(data={
            "success": True,
            "code": 200,
            "msg": "点赞成功",
            "likes": instance.likes,
        }, status=status.HTTP_200_OK)
