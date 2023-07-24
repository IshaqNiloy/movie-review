from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from applibs import response_helper, response_messages
from .models import User
from .serializers import (
    UserViewSerializer,
)


class UserView(APIView):
    permission_classes = [IsAdminUser]

    def __init__(self):
        super(UserView, self).__init__()
        self.request_data = None
        self.serializer = UserViewSerializer
        self.model = User
        self.args = None
        self.kwargs = None

    def post(self, request, *args, **kwargs):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)

            if self.serializer.is_valid():
                first_name = self.serializer.validated_data.get('first_name')
                last_name = self.serializer.validated_data.get('last_name')
                username = self.serializer.validated_data.get('username')
                email = self.serializer.validated_data.get('email')
                password = self.serializer.validated_data.get('password')

                # Looking for duplicate email
                duplicate_email = self.model.objects.filter(email=email)

                if len(duplicate_email) != 0:
                    return response_helper.success_response(message=response_messages.DUPLICATE_EMAIL)

                user = self.model.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                      password=password, email=email)

                response_data = {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "email": user.email,
                    "is_superuser": user.is_superuser,
                    "is_active": user.is_active,
                    "is_staff": user.is_staff,
                    "is_admin": user.is_admin,
                    "is_password_reset": user.is_password_reset,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                }

                return response_helper.success_response(message=response_messages.USER_CREATE_SUCCESS,
                                                        data=response_data)

            else:
                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA,
                                                      details=self.serializer.errors)

        except IntegrityError as e:
            return response_helper.error_response(message=response_messages.USER_ALREADY_EXIST)
        except Exception as e:
            return response_helper.error_response(message=response_messages.USER_CREATE_FAILED, details=str(e))

