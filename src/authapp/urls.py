from django.urls import path, include
import authapp.views as views

urlpatterns = [
    path("", views.Home.as_view(), name="home")
]