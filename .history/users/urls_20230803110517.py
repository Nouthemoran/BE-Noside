from django.urls import path
from .views import RegisterView, class ModelNameList(ListView):
    model = ModelName
    context_object_name = ''
    template_name=''

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', .as_view())
]
