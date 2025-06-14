from django.urls import path, include
from .views import *


app_name = "user_login"

urlpatterns = [
    path("", CustomLoginView.as_view(), name="login"),
    path("index/", index, name="index"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("signup/", CustomSignupView.as_view(), name="signup"),
    path("password_change/", CustomPasswordChangeView.as_view(), name="password_change"),
]