from django.urls import path, include
from .views import CustomLoginView, index


app_name = "user_login"

urlpatterns = [
    path("", CustomLoginView.as_view(), name="login"),
    path("index/", index, name="index"),
]