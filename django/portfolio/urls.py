from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.ProjectListView.as_view(), name='portfolio'),
]
