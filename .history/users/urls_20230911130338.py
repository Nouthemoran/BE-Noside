from django.urls import path
from . views import RegisterView, LoginView, UserView, LogoutView, UserUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path("user/", UserView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),

]
