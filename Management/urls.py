from django.urls import path
from . import views

app_name = 'Management'

urlpatterns = [
    path("top/", views.top, name="top")
]