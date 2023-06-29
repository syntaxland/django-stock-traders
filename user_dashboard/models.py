from django.db import models

class TraderData(models.Model):
    trader = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(default="100.00", max_digits=10, decimal_places=2)
    profit_loss = models.JSONField(default=list)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

class AdminDashboardData(models.Model):
    total_profit = models.FloatField()
    total_loss = models.FloatField()
    highest_profit_trader = models.CharField(max_length=100)
    lowest_profit_trader = models.CharField(max_length=100) 
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

