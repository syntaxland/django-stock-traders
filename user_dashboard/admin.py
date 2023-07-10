from django.contrib import admin
from . import models


@admin.register(models.TraderData)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'trader', 'profit_loss', 'timestamp')

@admin.register(models.AdminDashboardData)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_profit', 'total_loss', 'highest_profit_trader', 'lowest_profit_trader', 'timestamp')
