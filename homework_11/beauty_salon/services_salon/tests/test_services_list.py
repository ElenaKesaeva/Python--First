"""
Tests
"""
from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from services_salon.models import Service


class ServicesSalonListTestCase(TestCase):
    """
    Services_salon test
    """
    fixtures = [
        "service.fixture.json"
    ]

    def test_list_services_salon(self):
        """
        test list
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
        for service1, service2 in zip(services_salon, services_in_context):
            self.assertEqual(service1.pk, service2.pk)
