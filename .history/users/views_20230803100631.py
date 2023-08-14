from rest_framework.views import APIView
from .serializers import UserSerializer
# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer
