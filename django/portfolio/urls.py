from django.urls import path
from . import views

urlpatterns = [
    path('browse/authors/', views.ProjectListView.as_view(), name='browse-authors-list'),
]
