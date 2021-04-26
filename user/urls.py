from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign_up/', views.signup, name='sign_up'),
]