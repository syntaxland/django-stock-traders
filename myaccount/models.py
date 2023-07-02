from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=20, unique=True)
#     email_otp = models.CharField(max_length=6, null=True)
#     is_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email'
#     # USERNAME_FIELD = 'username'

#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = 'User Profile'

#     def str(self):
#         return f'{self.user.username} | {self.user.email}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True) 
    email_otp = models.CharField(max_length=6, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    # USERNAME_FIELD = 'username'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User Profile'

    def str(self):
        return f'{self.username} | {self.email}'
    

