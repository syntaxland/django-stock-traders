# Generated by Django 4.2.2 on 2023-06-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
