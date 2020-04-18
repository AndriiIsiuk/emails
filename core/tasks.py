from typing import List

from core.models import Email
from core.services.mails import send_email
from emails.celery_app import app


@app.task
def celery_send_created_email(email_pk: int) -> None:
    """Sending new email task with SENT status"""
    email = Email.objects.get(pk=email_pk)
    send_email(email)


@app.task
def celery_send_all_pending(pending_emails: List[int]) -> None:
    """Sending all emails with PENDING status"""
    print(11111111111111111111111111111111111111111111111111111111111, pending_emails)
    for pk in pending_emails:
        email = Email.objects.get(pk=pk)
        send_email(email)
        email.status = Email.SENT
        email.save()
