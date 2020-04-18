from rest_framework import serializers

from .models import Attachment, Email


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ("attachment", "id")


class EmailSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(read_only=True, many=True)

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
            "attachments",
        )


class EmailCreateSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        files = validated_data["files"]
        del validated_data["files"]

        email = Email.objects.create(**validated_data)

        attachments = []
        for attachment in files.values():
            attachments.append(Attachment(attachment=attachment, email=email))
        Attachment.objects.bulk_create(attachments)

        return email
