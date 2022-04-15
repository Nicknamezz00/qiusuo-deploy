import os

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

import backend.settings


@require_http_methods(["POST"])
def upload_avatar(request):
    """
    Uploads a avatar to the server.
    """
    if request.method == 'POST':
        if request.FILES['avatar']:
            if request.FILES['avatar'].size < 1024 or request.FILES['avatar'].size > 1024 * 1024 * 2:
                return JsonResponse({
                    'status': 'error',
                    'message': '头像大小在1k和2MB之间哦.',
                }, status=400)
            handle_file(request.FILES['avatar'], str(request.FILES['avatar'].name), '/media/avatar/')
            return JsonResponse({
                'status': 'success',
                'url': '/media/avatar/' + str(request.FILES['avatar'].name),
            }, status=200)
        else:
            return JsonResponse({
                'status': 'failed',
                'message': 'No file uploaded.',
            }, status=400)


def handle_file(file, filename, path):
    path = os.getcwd() + path
    print(path)
    if not os.path.exists(path):
        os.makedirs(path)
    print(path + filename)
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
