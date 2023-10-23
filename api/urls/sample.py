from django.urls import path
from api.views.sample import SampleView

urlpatterns = [
    path("", SampleView.as_view(), name="Hello world!"),
]