from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class SampleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Hello World!'}, status=status.HTTP_200_OK)