# finances/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import IPOListView, IPOByStatusView, IPODetailView

urlpatterns = [
    path('', views.landing_page, name='landing'),
    
    # Admin panel
    path('admin-panel/login/', views.admin_login, name='admin-login'),
    path('admin-panel/signup/', views.admin_signup, name='admin-signup'),
    path('admin-panel/forgot-password/', views.forgot_password, name='admin-forgot'),
    path('admin-panel/dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('admin-panel/ipos/', views.upcoming_ipos_view, name='ipo-list'),
    path('admin-panel/ipos/register/', views.register_ipo, name='ipo-register'),

    # REST API
    path('ipos/', IPOListView.as_view(), name='ipo-list-api'),
    path('ipos/status/<str:status>/', IPOByStatusView.as_view(), name='ipo-by-status'),
    path('ipos/<int:id>/', IPODetailView.as_view(), name='ipo-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
