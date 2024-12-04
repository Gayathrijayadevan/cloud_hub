from django.urls import path
from . import views

urlpatterns=[
    path('',views.chub_login),
    path('register',views.register),
    path('home',views.home),
    path('support',views.support),
    path('logout',views.logout),

]