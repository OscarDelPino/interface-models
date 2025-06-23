from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 

#from .forms import CustomUserRegisterForm
from .models import UserProfile


# Create your views here.
class CustomSignupView(generic.CreateView):
    template_name = "user_login/registration/signup.html"
    #form_class = CustomUserRegisterForm
    # fields = ['name', 'lastname', 'username', 'email', 'company', 'pets', 'password1', 'password2']
    success_url = reverse_lazy('user_login:login')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        response = super().form_valid(form)
        age = form.cleaned_data['age']
        country = form.cleaned_data['country']
        city = form.cleaned_data['city']
        company = form.cleaned_data['company']
        position = form.cleaned_data['position']
        UserProfile.objects.create(user=self.object, age=age, country=country, city=city, company=company, position=position)
        print(response)
        return response

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

@method_decorator(login_required(login_url='user_login:login'), name='dispatch')
class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = "user_login/registration/password_change.html"
    success_url = reverse_lazy('user_login:login')
    
    def form_valid(self, form):
        return super().form_valid(form)

def index(request):
    return render(request, 'user_login/index.html')


def profile(request):
    
    return render(request, 'user_login/perfil/user_data.html')