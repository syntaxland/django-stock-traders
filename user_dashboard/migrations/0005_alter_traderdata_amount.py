# Generated by Django 4.1.9 on 2023-06-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0004_traderdata_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traderdata',
            name='amount',
            field=models.DecimalField(decimal_places=2, default='100.00', max_digits=10),
        ),
    ]
