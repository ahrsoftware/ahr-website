from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('services/', views.ServicesView.as_view(), name='services'),
]
