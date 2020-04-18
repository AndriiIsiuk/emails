from django.db import transaction
from rest_framework import viewsets

from core.models import Email
from core.serializers import EmailSerializer, EmailCreateSerializer


class EmailsViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return EmailCreateSerializer
        return EmailSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(files=self.request.FILES)
