
from django.views.generic import DetailView

from services_salon.models import Service


class Services_salonDetailsTestCase(DetailView):
    fixtures = ["service.fixture.json",
                "details.fixture.json"
                ]

    def test_details_services_salon(self, **kwargs):
        context = super().test_details_services_salon(**kwargs)
        # Add in a QuerySet of all the books
        context['services_salon'] = Service.objects.all()
        return context









