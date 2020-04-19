from django.test import TestCase

from core.serializers import (
    EmailSerializer,
    EmailCreateSerializer,
    EmailStatusSerializer,
)


class EmailSerializerTests(TestCase):
    def test_contains_expected_fields_email_serializer(self):
        cart_ser = EmailSerializer()
        fields = {
            "id",
            "sender",
            "recipients",
            "title",
            "message",
            "status",
            "priority",
            "attachments",
        }
        self.assertCountEqual(cart_ser.fields, fields)

    def test_contains_expected_fields_email_create_serializer(self):
        cart_ser = EmailCreateSerializer()
        fields = {
            "id",
            "sender",
            "recipients",
            "title",
            "message",
            "status",
            "priority",
        }
        self.assertCountEqual(cart_ser.fields, fields)

    def test_contains_expected_fields_email_status_serializer(self):
        cart_ser = EmailStatusSerializer()
        fields = {"id", "status"}
        self.assertCountEqual(cart_ser.fields, fields)
