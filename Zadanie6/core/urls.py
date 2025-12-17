from django.urls import path
from . import views

urlpatterns = [
    path('api/greet/', views.greet, name='greet_api'),
]