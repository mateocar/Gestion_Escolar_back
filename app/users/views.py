from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class UserregistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


