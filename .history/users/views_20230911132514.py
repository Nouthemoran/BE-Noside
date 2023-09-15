import random
import subprocess


from course.models import OTP
from rest_framework import generics
from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.core.mail import send_mail
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import status, APIView
from rest_framework.generics import GenericAPIView

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

class LoginView(generics.CreateAPIView):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)
            username = list(User.objects.get(id=user.id).username)
            username_string = "".join(username)
            # subprocess.run('py manage.py flushexpiredtokens')
            return Response(
                {
                    "username": username_string,
                    "access_token": str(access_token),
                    "refresh_token": str(refresh_token),
                }

                , status=status.HTTP_200_OK)
        return Response({"error": "Username atau Password Salah!"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):

    authentication_classes = [JWTAuthentication]
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['refresh_token'],
        properties={
            'refresh_token': openapi.Schema(type=openapi.TYPE_STRING)
        }
    ))
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            # subprocess.run('py manage.py flushexpiredtokens')
            return Response({"detail": "Logout Berhasil!"})
        except Exception as e:
            return Response({"detail": "Token Tidak Valid!"})

class SendOTPView(GenericAPIView):

    serializer_class = SendOTPSerializer

    @csrf_exempt
    def post(self, request):
        data = self.request.data
        email = data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with email does not exist.'}, status=404)

        # Generate OTP
        otp = str(random.randint(100000, 999999))

        # Save OTP ke database
        otp_obj, created = OTP.objects.update_or_create(
            email=email, 
            defaults={
                'otp': otp,
                'created_at': timezone.now()
            })

        # Kirim otp ke user
        from_email = 'Median Talenta Raya', settings.EMAIL_HOST_USER
        subject = 'OTP Untuk Mereset Password Anda.'
        message = f'OTP Milikmu : {otp}. akan kadaluarsa dalam 10 menit.'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'detail': 'OTP dikirim.'})


class VerifyOTPAPIView(GenericAPIView):

    serializer_class = VerifyOTPSerializer

    @csrf_exempt
    def post(self, request):
        data = self.request.data
        email = data['email']
        otp = data['otp']

        User = get_user_model()
        user = User.objects.get(email=email)
        try:
            otp_obj = OTP.objects.get(email=email, otp=otp)
        except OTP.DoesNotExist:
            return JsonResponse({'error': 'Invalid OTP!.'}, status=400)

        # Cek jika otp kadaluarsa
        if otp_obj.is_expired():
            return JsonResponse({'error': 'OTP telah kadaluarsa!.'}, status=400)

        refresh = RefreshToken.for_user(user)
        response = JsonResponse({'detail': 'OTP terverifikasi.'}, status=200)
        response.set_cookie(key='refresh_token', value=str(refresh), httponly=False)
        # response.set_cookie(key='access_token', value=str(refresh.access_token), httponly=True)

        # Verifikasi OTP
        otp_obj.is_verified = True
        otp_obj.save()
        
        return response


class ChangePasswordView(GenericAPIView):

    serializer_class = ChangePasswordSerializer

    def post(self, request):
        # Get password baru
        data = self.request.data
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        # Validasi password baru
        if not password:
            return Response({'detail': 'Password tidak boleh Kosong!'}, status=status.HTTP_400_BAD_REQUEST)
        if password != confirm_password:
            return Response({'detail': 'Password tidak sesuai!'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate access token menggunakan refresh token
        refresh = request.COOKIES.get('refresh_token')
        if not refresh:
            return Response({'detail': 'Refresh token not found.'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = RefreshToken(refresh)
            token.verify()
        except Exception:
            return Response({'detail': 'Invalid refresh token.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Set password baru untuk user
        User = get_user_model()
        user = User.objects.get(id=token['user_id'])
        user.set_password(password)
        user.save()

        # Generate access token baru
        new_refresh = RefreshToken.for_user(user)
        response = Response({'detail': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        response.set_cookie(key='access_token', value=str(new_refresh.access_token), httponly=True)

        return response
    

class TokenRefreshView(APIView):
    serializer_class = AccTokenRefreshSerializer
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.views import APIView
# from .serializers import UserSerializer
# from rest_framework.response import Response
# from rest_framework.exceptions import AuthenticationFailed
# from .models import User
# from rest_framework import generics

# import logging
# from django.contrib.auth.hashers import make_password
# import jwt, datetime

# # Create your views here.
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

# logger = logging.getLogger(__name__)


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']

#         logger.debug(f"Login attempt: username={username}, password={password}")

#         user = User.objects.filter(username=username).first()
        
#         if user is None:
#             logger.warning(f"User not found for username: {username}")
#             raise AuthenticationFailed('User not found')
        
#         if not user.check_password(password):
#             logger.warning(f"Invalid password for user: {user}")
#             raise AuthenticationFailed('incorrect password')
        
#         payload = {
#             'id': user.id,
#             'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=40),
#             'iat': datetime.datetime.utcnow() 
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256')

#         response = Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }

#         return response
    
# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('unauthenticated')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('unauthenticated')

#         user = User.objects.filter(id=payload['id']).first()
#         if not user:
#             raise AuthenticationFailed('user not found')


#         serializer = UserSerializer(user)

#         return Response(serializer.data)
    
# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             "message": 'success'
#         }

#         return response


# class UserUpdateView(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def perform_update(self, serializer):
#         if 'password' in self.request.data:
#             password = make_password(self.request.data['password'])
#             serializer.save(password=password)
#         else:
#             serializer.save()

