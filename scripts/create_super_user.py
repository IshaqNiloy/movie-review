"""
python3 manage.py runscript create_super_user
"""

from django.conf import settings
from django.contrib.auth.models import User


def run():
    if settings.DA_ENVIRONMENT != 'development':
        print('This script can only be run in development environment.')
        return

    try:
        username = 'admin'
        password = 'admin'
        email = 'admin@example.com'

        user = User.objects.create_superuser(username=username, password=password, email=email)

        if user is None:
            print('Super user could not be created.')
        else:
            print('Super user created.')

    except Exception as err:
        print('Super user could not be created.', err)
