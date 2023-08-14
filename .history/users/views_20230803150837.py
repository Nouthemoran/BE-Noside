from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import logging
from django.contrib.auth.hashers import make_password
import jwt, datetime

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

logger = logging.getLogger(__name__)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        logger.debug(f"Login attempt: email={email}, password={password}")

        user = User.objects.filter(email=email).first()
        
        if user is None:
            logger.warning(f"User not found for email: {email}")
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            logger.warning(f"Invalid password for user: {user}")
            raise AuthenticationFailed('incorrect password')
        
        payload = {
            'id': user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=40),
            'iat': datetime.datetime.utcnow() 
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('user not found')


        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):


