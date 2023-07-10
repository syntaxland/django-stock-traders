from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

from django.utils.crypto import get_random_string
import random
import string


from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    email = models.EmailField(max_length=40, unique=True)
    phone_number = PhoneNumberField(max_length=14, blank=True)
    # email_otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images/avatars/', blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

    #     USERNAME_FIELD = 'email'
    #     REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        default_related_name = 'profile'
