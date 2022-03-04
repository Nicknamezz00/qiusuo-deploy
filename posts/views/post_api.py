from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.filters import PostFilter
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_class = PostFilter

