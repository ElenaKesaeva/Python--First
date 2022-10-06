from django.shortcuts import render, get_object_or_404

from services_salon.models import Service


def index(request):
    context = {
        "services_salon": Service.objects.order_by("pk").all()
    }
    return render(request=request, template_name="services_salon/index.html", context=context)


def details(request, pk):
    context = {
        "service": get_object_or_404(Service.objects.select_related("details"), pk=pk)
    }
    return render(request=request, template_name="services_salon/details.html", context=context)
