from django.urls import path
from . import views

app_name = "authsys"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path("signin/", views.SignInView.as_view(), name='signin'),
    path("signout/", views.SignOutView.as_view(), name='signout'),
]