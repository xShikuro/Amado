from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("shop/", views.shop_view, name="shop"),
]
