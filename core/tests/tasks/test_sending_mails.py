from django.test import TestCase

from core.models import Email
from core.tasks import celery_send_all_pending
from core.tests.factories.email import EmailFactory


class TestCelerySendTasks(TestCase):
    def setUp(self):
        self.email = EmailFactory(status=Email.PENDING)

    def test_send_emails_pending(self):
        for _ in range(2):
            EmailFactory(status=Email.PENDING)

        pending = Email.objects.filter(status=Email.PENDING).values_list(
            "pk", flat=True
        )
        self.assertEqual(len(pending), 3)

        celery_send_all_pending(pending)

        self.assertEqual(Email.objects.filter(status=Email.SENT).count(), 3)
        self.assertEqual(Email.objects.filter(status=Email.PENDING).count(), 0)
