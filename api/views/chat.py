from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from api.chatbot_model.chatbot import ai_chat

class ChatView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            ai_response = ai_chat(data["message"])
            return Response({'message': f'{ai_response}'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)