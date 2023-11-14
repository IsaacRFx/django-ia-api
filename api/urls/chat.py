from django.urls import path
from api.views.chat import ChatView

urlpatterns = [
    path("conversation/", ChatView.as_view(), name="Hello world!"),
]