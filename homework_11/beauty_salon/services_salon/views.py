"""
Views
"""
from django.views.generic import ListView, DetailView
from services_salon.models import Service


class ServicesSalonListView(ListView):
    """
    List view
    """
    template_name = "services_salon/index.html"
    context_object_name = "services_salon"
    queryset = (
        Service.objects.order_by("pk").all()
    )


class ServiceDetailView(DetailView):
    """
    Detail view
    """
    template_name = "services_salon/details.html"
    context_object_name = "service"
    queryset = (
        Service
        .objects
        .select_related("details"))
