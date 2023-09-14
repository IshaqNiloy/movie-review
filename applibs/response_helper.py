from rest_framework.response import Response
from rest_framework import status


def success_response(message: str, lang: str, data=None, details=None) -> Response:
    return Response({
        'message': message,
        'lang': lang,
        'data': data,
        'details': details
    }, status=status.HTTP_200_OK)


def error_response(message: str, lang: str, data=None, details=None) -> Response:
    return Response({
        'message': message,
        'lang': lang,
        'data': data,
        'details': details
    }, status=status.HTTP_400_BAD_REQUEST)
