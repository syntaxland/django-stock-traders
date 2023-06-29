from django.contrib import admin
from . import models


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'username', 
                    'first_name', 'last_name', 
                    'email', 'phone_number', 
                    'is_verified', 'created_at', 
                    )
admin.site.register(models.Profile, ProfileAdmin)

