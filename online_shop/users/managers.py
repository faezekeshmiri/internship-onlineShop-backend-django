from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where phone number is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone, password, **extra_fields):
        """
        Create and save a User with the given phone and password.
        """
        if not phone:
            raise ValueError(_('The phone number must be set'))
        user = self.model(phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_producer', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)

    def create_staffuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_producer', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('staff must have is_staff=True.'))
        return self.create_user(phone, password, **extra_fields)

    def create_producer(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_producer', True)

        if extra_fields.get('is_producer') is not True:
            raise ValueError(_('producer must have is_producer=True.'))
        return self.create_user(phone, password, **extra_fields)

