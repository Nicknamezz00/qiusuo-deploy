import os

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend import settings

if settings.ENV_DEFINE == 'online':
    prefix = 'https://qiusuo-1622447-1309638607.ap-shanghai.run.tcloudbase.com/'
else:
    prefix = 'http://127.0.0.1:8000/'


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
        'subject-manage': prefix + 'subject-manage/',
        'informations': prefix + 'informations/',
        'feedback': prefix + 'feedback/',
        'examine': prefix + 'examine/',
    })
