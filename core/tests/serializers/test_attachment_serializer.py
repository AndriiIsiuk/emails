from django.test import TestCase

from core.serializers import AttachmentSerializer


class AttachmentSerializerTests(TestCase):
    def test_contains_expected_fields_attachment_serializer(self):
        cart_ser = AttachmentSerializer()
        fields = {"attachment"}
        self.assertCountEqual(cart_ser.fields, fields)
