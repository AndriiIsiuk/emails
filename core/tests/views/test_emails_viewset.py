from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Email
from core.tests.factories.email import EmailFactory


def _fake_celery_send_all_pending(ids):
    return True


class TestItemsApiView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.emails_list_url = reverse("core:email-list")
        cls.emails_send_pending_url = reverse("core:email-send-all-pending")

    def setUp(self):
        self.email = EmailFactory(status=Email.PENDING)
        self.email2_data = {
            "sender": "test1@send.it",
            "recipients": ["one@one.com", "two@two.com"],
            "title": "Testing mail",
            "message": "Test content",
        }

    def test_emails_list(self):
        response = self.client.get(self.emails_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)

    def test_emails_create(self):
        email_data = self.email2_data
        email_data["status"] = Email.SENT

        emails = Email.objects.all().count()
        self.assertEqual(emails, 1)
        response = self.client.post(self.emails_list_url, email_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        emails = Email.objects.all().count()
        self.assertEqual(emails, 2)
        last = Email.objects.all().last()
        self.assertEqual(last.status, Email.SENT)

    def test_emails_create_default_status(self):
        response = self.client.post(self.emails_list_url, self.email2_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        last = Email.objects.all().last()
        self.assertEqual(last.status, Email.PENDING)

    def test_email_details(self):
        response = self.client.post(self.emails_list_url, self.email2_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        emails_detail_url = reverse("core:email-detail", args=(response.json()["id"],))

        response_detail = self.client.get(emails_detail_url)
        self.assertEqual(response_detail.status_code, status.HTTP_200_OK)

        email = response_detail.json()
        self.assertEqual(email["sender"], self.email2_data["sender"])
        self.assertEqual(email["title"], self.email2_data["title"])
        self.assertEqual(email["message"], self.email2_data["message"])
        self.assertEqual(email["status"], Email.PENDING)
        self.assertEqual(email["priority"], Email.LOW)

        self.assertListEqual(
            sorted(email["recipients"]), sorted(self.email2_data["recipients"])
        )
        self.assertCountEqual(email["recipients"], self.email2_data["recipients"])

    def test_emails_create_without_duplicated_recipients(self):
        email_with_duplicated_recipients = self.email2_data
        email_with_duplicated_recipients["recipients"] = [
            "one@one.com",
            "two@two.com",
            "two@two.com",
            "two@two.com",
            "two@two.com",
        ]

        response = self.client.post(
            self.emails_list_url, email_with_duplicated_recipients
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        last = Email.objects.all().last()
        self.assertEqual(sorted(last.recipients), ["one@one.com", "two@two.com"])

    def test_email_status(self):
        email = EmailFactory(status=Email.SENT)
        email_status_url = reverse("core:email-show-email-status", args=(email.id,))
        response = self.client.get(email_status_url)
        self.assertDictEqual(response.json(), {"id": email.id, "status": email.status})
