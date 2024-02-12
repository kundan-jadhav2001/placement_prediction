from django.urls import path
from model import views

urlpatterns = [
    path('',views.home),
    path('signinup',views.signinup)
    
]
