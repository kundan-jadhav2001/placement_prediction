from django.urls import path
from model import views

urlpatterns = [
    path('',views.home),
    path('signinup',views.signinup),
    path('contact',views.contact),
    path('course',views.course),
    path('blog',views.blog),
    path('about',views.about),
    path('confirmsignup',views.confirmsignup),
    path('confirmsignin',views.confirmsignin),
    path('predictionpage', views.predictionpage),
    path('predict', views.predict),
    path('report', views.report),
    path('front', views.front),
]
