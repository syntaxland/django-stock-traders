from django.urls import path
from user_dashboard import views

from .views import AdminDashboardPDFView

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('admin_dashboard/pdf/', views.admin_dashboard_pdf, name='admin_dashboard_pdf'),
    path('admin_dashboard/pdf/', AdminDashboardPDFView.as_view(), name='admin_dashboard_pdf'),
]
