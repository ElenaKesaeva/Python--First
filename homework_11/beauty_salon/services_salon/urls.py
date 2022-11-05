"""
Urls
"""
from django.urls import path
from .views import ServicesSalonListView, ServiceDetailView


# app_name = "services_salon"
APP_NAME = "services_salon"

urlpatterns = [
    # path("", index, name="index"),
    # path("<int:pk>/", details, name="details"),
    path("", ServicesSalonListView.as_view(), name="index"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="details")
    ]
