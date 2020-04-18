from django.db import models
from django.db.models import EmailField
from django.contrib.postgres.fields import ArrayField


class Email(models.Model):
    PENDING = "PENDING"
    SENT = "SENT"

    STATUSES = ((PENDING, "Pending"), (SENT, "Sent"))

    LOW = "LOW"
    HIGH = "HIGH"

    PRIORITY = ((LOW, "Low"), (HIGH, "High"))

    sender = models.EmailField(max_length=64)
    recipients = ArrayField(EmailField(max_length=64))
    title = models.CharField(max_length=256)
    message = models.TextField(blank=False)
    status = models.CharField(max_length=16, choices=STATUSES, default=PENDING)
    priority = models.CharField(max_length=8, choices=PRIORITY, default=LOW)


class Attachment(models.Model):
    attachment = models.FileField()
    email = models.ForeignKey(
        Email, related_name="attachments", on_delete=models.CASCADE
    )
