from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from services_salon.models import Service


class Services_salonDetailsTestCase(TestCase):
    fixtures = [
        "details.fixture.json"
    ]

    def test_details_services_salon(self):

        url = reverse("services_salon:details", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        service = (Service.objects.select_related("details"))
        service_in_context = response.context["details"]
        self.assertEqual(len(service), len(service_in_context))
        for s1, s2 in zip(service, service_in_context):
            self.assertEqual(s1.pk, s2.pk)


