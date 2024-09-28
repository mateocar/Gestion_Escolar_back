from .models import User
from .serializers import UserSerializer, ObtainTokenSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            response_data = {
                'full_name': serializer.data['full_name'],
                'email': serializer.data['email'],
                'username': serializer.data['username'],
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(TokenObtainPairView):
    serializer_class = ObtainTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, 
            context={'request': request}
        )

        try:
            serializer.is_valid()
            data = serializer.validated_data
            user = serializer.user
            data['full_name'] = user.full_name
            response_data = {
                'refresh': data['refresh'],
                'access': data['access'],
                'full_name': data['full_name']
            }
            return Response(
                response_data,
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AuthenticatedUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(f"El usuario {request.user.username} con el rol {request.user.role}", status=status.HTTP_200_OK)
