from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

prefix = 'https://api.qiusuo-mc.cn/'


@api_view(['GET'])
@permission_classes([AllowAny])
def root(request):
    return Response({
        'api-version': '1.2',
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
