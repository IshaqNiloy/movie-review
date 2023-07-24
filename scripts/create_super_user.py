"""
python3 manage.py runscript create_super_user
"""

from django.conf import settings
from user_management.models import User


def run():
    if settings.DA_ENVIRONMENT != 'development':
        print('This script can only be run in development environment.')
        return

    try:
        first_name = 'admin'
        last_name = 'admin'
        username = 'admin'
        password = 'admin'
        email = 'admin@example.com'

        user = User.objects.create_superuser(first_name=first_name, last_name=last_name, username=username,
                                             password=password, email=email)

        if user is None:
            print('Super user could not be created.')
        else:
            print('Super user created.')

    except Exception as err:
        print('Super user could not be created.', err)
