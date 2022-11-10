"""
Test
"""
from http import HTTPStatus
from django.test import TestCase

from django.urls import reverse

from services_salon.models import Service


class Services_salonListTestCase(TestCase):
    fixtures = [
        "service.fixture.json"
    ]

    def test_list_services_salon(self):
        """
        test service list
        :return:
        """
        url = reverse("services_salon:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        services_salon = (
            Service.objects.order_by("pk").all()
        )
        services_in_context = response.context["services_salon"]
        self.assertEqual(len(services_salon), len(services_in_context))
        for s1, s2 in zip(services_salon, services_in_context):
            self.assertEqual(s1.pk, s2.pk)
