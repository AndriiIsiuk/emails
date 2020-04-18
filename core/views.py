from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import Email, Attachment
from core.serializers import EmailSerializer, EmailCreateSerializer
from core.services.mails import send_email


class EmailsViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return EmailCreateSerializer
        return EmailSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            mail = serializer.save(files=self.request.FILES)
        print(
            55555555555555555555555555555555555555555555555555557777, mail.attachments
        )

        mail = Email.objects.last()
        attachments = Attachment.objects.last()
        print(66666666666666, mail, "|||", attachments.attachment)
        send_email(mail)

    # TODO - send all emails
    # TODO - select_related("attachments")
