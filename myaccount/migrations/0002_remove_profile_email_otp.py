# Generated by Django 4.2.2 on 2023-07-08 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_otp',
        ),
    ]
