from django.urls import path
from . import views

urlpatterns = [
    path("mealplaner",views.mealplaner,name="mealplaner"),
    path('',views.index,name="index"),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("menu",views.menu,name='menu'),
     path("about",views.about,name='about')
]
