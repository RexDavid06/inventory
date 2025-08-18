from django.shortcuts import render
from .forms import SignUpForm, SignInForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = "authsys/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("authsys:login")


class SignInView(LoginView):
    template_name = "authsys/signin.html"
    form_class = SignInForm



