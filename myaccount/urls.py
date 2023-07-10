from django.urls import path
from . import views
from .views import AccountDeleteView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    # path('forget-password/', views.forget_password, name='forget_password'),
    path('account/delete/', AccountDeleteView.as_view(), name='account-delete'),

    # path('reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset_password'),
    # path('send-password-reset-link/', views.send_password_reset_link, name='send_password_reset_link'),
    
]


