from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Email
from core.serializers import EmailSerializer, EmailCreateSerializer
from core.tasks import celery_send_created_email, celery_send_all_pending


class EmailsViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return EmailCreateSerializer
        return EmailSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            mail = serializer.save(files=self.request.FILES)

        if mail.status == Email.SENT:
            celery_send_created_email.delay(mail.pk)

    @action(detail=False, methods=["POST"])
    def send_all_pending(self, request):
        pending = Email.objects.filter(status=Email.PENDING).values_list(
            "pk", flat=True
        )
        celery_send_all_pending.delay(list(pending))
        return Response(status=status.HTTP_204_NO_CONTENT)
