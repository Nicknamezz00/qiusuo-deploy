from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users.urls import user_api_router

prefix = 'https://qiusuo-1622447-1309638607.ap-shanghai.run.tcloudbase.com/'


@api_view(['GET'])
@permission_classes([AllowAny])
def root(request):
    return Response({
        'swagger-doc': prefix + 'doc/',
        'docs': prefix + 'docs/',
        'operation-manage': prefix + 'operation-manage/',
        'user-manage': prefix + 'user-manage/',
        'post-manage': prefix + 'post-manage/',
        'comment-manage': prefix + 'comment-manage/',
    })
