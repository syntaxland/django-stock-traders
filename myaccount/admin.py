from django.contrib import admin
from . import models


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 
#                      'username',  'first_name', 'last_name', 'email', 
#                     'phone_number', 'is_verified', 'created_at', 
#                     )
# admin.site.register(models.Profile, ProfileAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'get_first_name', 'get_last_name', 
                    'get_email', 'phone_number', 'is_verified', 'created_at')

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    get_username.short_description = 'Username'
    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'
    get_email.short_description = 'Email'

admin.site.register(models.Profile, ProfileAdmin)
