from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from portal.serializer import auth_serializer
from utils.custom_responses import prepare_error_response


class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = auth_serializer.MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = auth_serializer.RegistrationSerializer


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        logout(request)
        data = {'message': 'logged out'}
        return Response(data=data, status=status.HTTP_200_OK)


class ProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            queryset = User.objects.get(id=self.request.user.id)
            serializer = auth_serializer.UserSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(prepare_error_response('Sorry! User must be login'), status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = auth_serializer.PasswordUpdateSerializer
