from django.db import models
from myaccount.models import Profile
from django.utils import timezone

import random
from django.utils.crypto import get_random_string
import string
# from django.contrib.auth import get_user_model

# User = get_user_model()

class EmailOtp(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def is_valid(self):
        # Check if the OTP is within the valid time range (15 minutes)
        return self.created_at >= timezone.now() - timezone.timedelta(minutes=15)

    # def generate_email_otp(self):
    #     self.email_otp = get_random_string(length=6)
    #     self.save()

    # def generate_email_otp(self):
    #     chars = string.ascii_uppercase + string.digits
    #     self.email_otp = ''.join(random.choices(chars, k=6))
    #     self.save()

    def generate_email_otp(self):
        self.email_otp = str(random.randint(100000, 999999))
        self.created_at = timezone.now()
        self.save()

    class Meta:
        default_related_name = 'email_otp'


