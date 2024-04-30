from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import CustomUserRegisterForm

# Create your views here.
class CustomSignupView(generic.CreateView):
    template_name = "user_login/registration/signup.html"
    form_class = CustomUserRegisterForm
    # fields = ['name', 'lastname', 'username', 'email', 'company', 'pets', 'password1', 'password2']
    success_url = reverse_lazy('user_login:login')

class CustomLoginView(auth_views.LoginView):
    template_name = "user_login/registration/login.html"
    next_page = "user_login:profile"

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form.
        First we are going to check if user is a super user, if so, we are going to redirect to admin page"""

        if self.request.user.is_superuser:
            admin_page = "admin:index"
            return reverse(admin_page)
        
        return self.get_default_redirect_url()

class CustomLogoutView(auth_views.LogoutView):
    template_name = "user_login/registration/logged_out.html"


def index(request):
    return render(request, 'user_login/index.html')

def profile(request):
    print(request.user.is_authenticated)
    print(request.user)
    print(request.user.is_superuser)
    print(request.META['HTTP_USER_AGENT'])
    print(request.META['REMOTE_ADDR'])
    print(request.META['SERVER_NAME'])
    return render(request, 'user_login/perfil/user_data.html')