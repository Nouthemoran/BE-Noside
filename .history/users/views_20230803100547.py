from rest_framework.views import APIView
from .serializers importUser
# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer =UserSerializer()