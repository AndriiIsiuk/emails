from django.db import transaction
from rest_framework import viewsets

from core.models import Email
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

        send_email(mail)

    # TODO - send all emails
    # TODO - select_related("attachments")
