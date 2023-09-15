"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/customers/', include('customers.urls')),
    path('api/repositories/', include('repositories.urls')),
    path('api/journals/', include('journals.urls')),
    path('api/conferences/', include('conferences.urls')),
    path("auth/login/", LoginView.as_view(), name='login'),
    path("auth/logout/", LogoutView.as_view(), name='logout'),
    path("auth/send-otp/", SendOTPView.as_view(), name='send-otp'),
    path("auth/verify-otp/", VerifyOTPAPIView.as_view(), name='send-otp'),
    path("auth/change-password/", ChangePasswordView.as_view(), name='change-password'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
