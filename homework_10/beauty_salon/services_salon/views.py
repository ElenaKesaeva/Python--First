from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from services_salon.models import Service


class Services_salonListView(ListView):
    template_name = "services_salon/index.html"
    # template_name = "animals/animal_list.html"
    context_object_name = "services_salon"
    queryset = (
        Service.objects.order_by("pk").all()
    )


class ServiceDetailView(DetailView):
    template_name = "services_salon/details.html"
    context_object_name = "service"
    queryset = (
        Service
        .objects
        .select_related("details"))
