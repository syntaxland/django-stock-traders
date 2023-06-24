from django.contrib import admin
from . import models

# admin.site.register(models.TraderData)
# admin.site.register(models.AdminDashboardData)

# OR using ModelAdmin

# class TraderDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'trader', 'profit_loss', 'timestamp')
#     prepopulated_fields = {'slug': ('title',), }
# admin.site.register(models.TraderData, TraderDataAdmin)

# class DashboardDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
# admin.site.register(models.AdminDashboardData, DashboardDataAdmin)

# OR using decorators


@admin.register(models.TraderData)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'trader', 'profit_loss', 'timestamp')

@admin.register(models.AdminDashboardData)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_profit', 'total_loss', 'highest_profit_trader', 'lowest_profit_trader', 'timestamp')
