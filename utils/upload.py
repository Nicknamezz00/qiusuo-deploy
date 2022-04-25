import os

from django.http import JsonResponse

from urllib.request import quote
from utils.CosSingleCilent import cos


def upload_avatar(request):
    """
    Uploads a avatar to the server.
    """
    if request.method == 'POST':
        if hasattr(request, 'FILES'):
            if request.FILES['avatar'].size < 1024 or request.FILES['avatar'].size > 1024 * 1024 * 2:
                return JsonResponse({
                    'status': 'error',
                    'message': '头像大小在1k和2MB之间哦.',
                }, status=400)
            file_path = handle_file(
                request.FILES['avatar'], str(
                    request.FILES['avatar'].name), '/media/avatar/')
            return JsonResponse({
                'status': 'success',
                'url': 'https://7072-prod-4gtr7e0o54f0f5ca-1309638607.tcb.qcloud.la/media/avatar/' + quote(str(
                    file_path)),
            }, status=200)
        else:
            return JsonResponse({
                'status': 'failed',
                'message': 'No file uploaded.',
            }, status=400)
    else:
        return JsonResponse({
            'status': 'failed',
            'message': 'only in post method',
        }, status=400)


def handle_file(file, filename, path):
    localpath = os.getcwd() + path
    if not os.path.exists(localpath):
        os.makedirs(localpath)
    with open(localpath + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return cos.write_file(filepath=path, filename=filename, localpath=localpath)

