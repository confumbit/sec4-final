from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("finishregister/", views.finishregister, name="finishregister"),
    path("finishlogin/", views.finishlogin, name="finishlogin"),
    path("login/", views.login, name="login"),
    path("profiles/", views.profiles, name="profiles"),
]
