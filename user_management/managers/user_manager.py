from django.db import models


class UserManager(models.Manager):
    
    def create_user(self, first_name, last_name, username, email):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email)
        )

        return user

    def create_superuser(self, first_name, last_name, username, email):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email)
        )

        user.is_superuser = True
        user.is_stuff = True
        user.is_admin = True
        user.is_password_reset = True

        return user
    