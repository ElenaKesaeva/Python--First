from django.urls import path

from .views import Services_salonListView, ServiceDetailView

app_name = "services_salon"

urlpatterns = [
    # path("", index, name="index"),
    # path("<int:pk>/", details, name="details"),
    path("", Services_salonListView.as_view(), name="index"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="details")
    ]