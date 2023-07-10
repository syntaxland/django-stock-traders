from django.contrib import admin
from .models import EmailOtp


class EmailOtpAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_otp', 'created_at')

admin.site.register(EmailOtp, EmailOtpAdmin)

