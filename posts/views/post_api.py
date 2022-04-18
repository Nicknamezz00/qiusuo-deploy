from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend import helper
from posts.filters import PostFilter
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer
from users import permissions as user_permisson


@permission_classes([PostPermission,
                     user_permisson.IsManualAuthenticatedOrReadOnly])
class PostViewSet(helper.MyModelViewSet):
    """
    帖子接口，需要权限。
        1. 'Basic Auth'
        2. JWT认证，请求头Authorization：JWT + 登陆返回的Token
    """
    # 最新的帖子
    queryset = Post.objects.all().order_by('created_at').reverse()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_class = PostFilter

    ordering_fields = ['created_at', 'likes']
    search_fields = ['=author__username', 'category', 'title']

    @action(methods=['POST'], detail=True,
            permission_classes=[IsAuthenticated])
    def thumbs_up(self, request, pk):
        """
        未实名和实名用户均可点赞。
        通过<pk>索引，对指定帖子点赞。
        暂时没有限制点赞次数（一个人可以让点赞数不停增加，maybe前端考虑限制一次，还要实现throttle）
        """
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
