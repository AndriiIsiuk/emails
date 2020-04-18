from rest_framework import serializers

from .models import Attachment, Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            "id",
            "sender",
            "recipients",
            "title",
            "message",
            "status",
            "priority",
        )


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ("id", "attachment", "email")
