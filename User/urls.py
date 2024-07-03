from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("signin", views.signin, name="signin"),
    path("signin_request", views.signin_request, name="signin_request"),
    path("signout", views.signout, name="signout"),
]
