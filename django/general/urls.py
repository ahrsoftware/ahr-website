from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome'),
    path('services/', views.ServicesTemplateView.as_view(), name='services'),
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies'),
]
