from django.urls import path
from . import views

app_name = 'Management'

urlpatterns = [
    path("top/", views.top, name="top"),
    path("detail/<int:id>",views.detail, name="detail"),
    path("detail/<int:id>/update",views.detail_update,name="detail_update"),
    path("portfolio/",views.portfolio, name="portfolio"),
]