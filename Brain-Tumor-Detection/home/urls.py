from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.base,name = "base"),
    # path("about",views.about,name = "about"),
    path("SignUp.html",views.SignUp,name = "SignUp"),
    path("login.html",views.login,name="login"),
    path("contact.html",views.contact,name="contact"),

]