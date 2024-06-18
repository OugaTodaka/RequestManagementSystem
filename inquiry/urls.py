from django.urls import path
from . import views


app_name = 'inquiry'

urlpatterns = [
    path("inquiry/", views.IndexView.as_view(), name="index"),
]