from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccessView.as_view(), name='contact-success'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('services/', views.ServicesView.as_view(), name='services'),
]
