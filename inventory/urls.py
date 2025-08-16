from django.urls import path 
from . import views

app_name = 'inventory'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("home/", views.HomeView.as_view(), name='home'),
    path("dashboard/", views.DashboardView.as_view(), name='dashboard'),
    path("add-item/", views.AddItemView.as_view(), name='add-item'),
    path("reports/", views.ReportsView.as_view(), name='reports'),
]