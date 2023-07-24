from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, first_name, last_name, username, password, email):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=self.normalize_email(email),
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_password_reset = True

        user.save(using=self._db)

        return user

    def create_user(self, first_name, last_name, username, password, email):
        user = self.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    