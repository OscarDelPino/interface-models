from django.urls import path, include
from .views import LoginView


app_name = "user_login"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
]