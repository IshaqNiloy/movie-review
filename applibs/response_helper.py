from rest_framework.response import Response
from rest_framework import status


def success_response(message: str, data=None, details=None) -> Response:
    return Response({
        'message': message,
        'data': data,
        'details': details
    }, status=status.HTTP_200_OK)


def error_response(message: str, data=None, details=None) -> Response:
    return Response({
        'message': message,
        'data': data,
        'details': details
    }, status=status.HTTP_400_BAD_REQUEST)
