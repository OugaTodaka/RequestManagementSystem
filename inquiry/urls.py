from django.urls import path
from . import views


app_name = 'inquiry'

urlpatterns = [
    path("inquiry/<int:id>", views.IndexView.as_view(), name="index"),
    path("inquiry/success",views.InquirysuccessView.as_view(),name="success")
]