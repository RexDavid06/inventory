from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "authsys"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path("signin/", views.SignInView.as_view(), name='signin'),
    path("signout/", views.LogoutView.as_view(next_page='authsys:signin'), name='signout'),
]