from django.contrib import admin
from django.urls import path, include
from finances import views as fin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse("Welcome to IPO Web App")),

    # Include app-level routes
    path('', include('finances.urls')),

    # Admin Panel Views
    path('admin-panel/login/', fin_views.admin_login, name='admin-login'),
    path('admin-panel/signup/', fin_views.admin_signup, name='admin-signup'),
    path('admin-panel/forgot-password/', fin_views.forgot_password, name='admin-forgot'),
    path('admin-panel/dashboard/', fin_views.admin_dashboard, name='admin-dashboard'),
    path('admin-panel/ipos/', fin_views.upcoming_ipos_view, name='ipo-list'),
    path('admin-panel/ipos/register/', fin_views.register_ipo, name='ipo-register'),
]
