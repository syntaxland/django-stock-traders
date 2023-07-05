from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('admin/', admin.site.urls),
    # Started apps
    path('', include('user_dashboard.urls')),
    path('', include('myaccount.urls')),
    path('', include('email_otp_auth.urls')),
    # path('', include('captcha_api.urls')),

    # Google OAuth paths
    # path('', TemplateView.as_view(template_name="login.html")),
    path('accounts/', include('allauth.urls')), 
    path('logout', LogoutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
