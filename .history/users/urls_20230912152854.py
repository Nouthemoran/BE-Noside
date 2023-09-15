from django.urls import path
from . views import RegisterView, LoginView, UserView, LogoutView, UserUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path("user/", UserView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    
    path("auth/login/", LoginView.as_view(), name='login'),
    path("auth/logout/", LogoutView.as_view(), name='logout'),
    path("auth/send-otp/", SendOTPView.as_view(), name='send-otp'),
    path("auth/verify-otp/", VerifyOTPAPIView.as_view(), name='send-otp'),
    path("auth/change-password/", ChangePasswordView.as_view(), name='change-password'),

    # 230324 - rahadianhadi - ubah ke endpoint /api/v1/
    path(f'{api_v1}/auth/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{api_v1}/get_csrf_token/', get_csrf_token, name='get_csrf_token'),

]
