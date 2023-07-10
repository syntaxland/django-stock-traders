from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('send-sms-otp/', views.send_sms_otp, name='send_sms_otp'),

    path('verify-sms-otp/', views.verify_sms_otp, name='verify_sms_otp'),
    path('verify-sms-otp/<str:phone>/', views.verify_sms_otp, name='verify_sms_otp'),
    # path('<str:phone>/', views.verify_sms_otp, name='verify_sms_otp'),

    path('welcome/', views.welcome, name='welcome'),
]
