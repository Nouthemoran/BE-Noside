from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view())
    path('L/', RegisterView.as_view())
]
