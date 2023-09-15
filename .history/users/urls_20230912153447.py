from django.urls import path
from .views import LoginView, LogoutView, SendOTPView, VerifyOTPAPIView, ChangePasswordView, TokenRefreshView, get_csrf_token


urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("send-otp/", SendOTPView.as_view(), name='send-otp'),
    path("verify-otp/", VerifyOTPAPIView.as_view(), name='send-otp'),
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),

    path('/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('/get_csrf_token/', get_csrf_token, name='get_csrf_token'),
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    # path("user/", UserView.as_view()),
    # path("logout/", LogoutView.as_view()),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    

]
