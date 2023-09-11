from django.urls import path
from . views import RegisterView, LoginView, UserView, LogoutView, UserUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path("user/", UserView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
