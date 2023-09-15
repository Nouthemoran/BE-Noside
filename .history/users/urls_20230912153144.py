from django.urls import path
from . import 


urlpatterns = [
    path("auth/login/", LoginView.as_view(), name='login'),
    path("auth/logout/", LogoutView.as_view(), name='logout'),
    path("auth/send-otp/", SendOTPView.as_view(), name='send-otp'),
    path("auth/verify-otp/", VerifyOTPAPIView.as_view(), name='send-otp'),
    path("auth/change-password/", ChangePasswordView.as_view(), name='change-password'),

    path(f'{api_v1}/auth/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{api_v1}/get_csrf_token/', get_csrf_token, name='get_csrf_token'),
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    # path("user/", UserView.as_view()),
    # path("logout/", LogoutView.as_view()),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    

]
