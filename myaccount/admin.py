from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileUserAdmin(UserAdmin):
    list_display = ('id', 'username',  'first_name', 'last_name', 'email', 'phone_number', 'is_verified', 'is_staff', 'created_at',)
    search_fields = ('email','username', 'first_name', 'last_name')
    ordering = ('id',)

admin.site.register(Profile, ProfileUserAdmin)
# admin.site.register(get_user_model(), ProfileUserAdmin)
# 
