from django.urls import path
from .views import send_password_reset_email, PasswordResetView

urlpatterns = [
    path('reset-password/<token>/', PasswordResetView.as_view(), name='password_reset'),
    path('forgot-password/', send_password_reset_email, name='password_reset_request'),
]
