from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.

class CustomLoginView(auth_views.LoginView):
    template_name = "user_login/registration/login.html"
    next_page = "user_login:index"
    


def index(request):
    print(request.user.is_authenticated)
    print(request.user)
    return render(request, 'user_login/index.html')