# finances/urls.py
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from finances import views as fin_views
from .views import IPOListView, IPOByStatusView, IPODetailView

urlpatterns = [
    path('', fin_views.landing_page, name='landing'),

    # Admin Auth
    path('admin-panel/login/', fin_views.admin_login, name='admin-login'),
    path('admin-panel/signup/', fin_views.admin_signup, name='admin-signup'),

    # Dashboard
    path('admin-panel/dashboard/', fin_views.admin_dashboard, name='admin-dashboard'),

    # IPO Views
    path('admin-panel/ipos/', fin_views.upcoming_ipos_view, name='ipo-list'),

    path('ipos/', IPOListView.as_view(), name='ipo-list-api'),
    path('ipos/status/<str:status>/', IPOByStatusView.as_view(), name='ipo-by-status'),
    path('ipos/<int:id>/', IPODetailView.as_view(), name='ipo-detail'),

    # Django Admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
