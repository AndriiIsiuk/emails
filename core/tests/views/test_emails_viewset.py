from django.urls import reverse
from rest_framework.test import APITestCase

from core.tests.factories.email import EmailFactory


class TestItemsApiView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item_url = reverse("core:email-list")

    def setUp(self):
        self.email = EmailFactory()

    def test_emails_list(self):
        response = self.client.get(self.item_url)
        print(response.json())
        self.assertEqual(len(response.json()["results"]), 1)
