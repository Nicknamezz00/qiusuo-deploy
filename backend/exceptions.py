from django.core.exceptions import ObjectDoesNotExist
from django.db import DataError
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, handler):
    response = exception_handler(exc, handler)

    if response is None:
        if isinstance(exc, DataError):
            response = Response(data={
                'code': 500,
                'error_msg': '数据库异常',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if isinstance(exc, Exception):
            response = Response(data={
                'code': 500,
                'msg': '有未处理的异常',
                'error_msg': exc.args,
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if isinstance(exc, ValidationError):
        response = Response(data={
            'code': 400,
            'error_msg': exc.detail
        }, status=status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, ObjectDoesNotExist):
        response = Response(data={
            'code': 400,
            'error_msg': exc.args,
        }, status=status.HTTP_400_BAD_REQUEST)

    return response
