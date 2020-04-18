from core.models import Email
from core.services.mails import send_email
from emails.celery_app import app


@app.task
def celery_send_created_email(email_pk: int) -> None:
    """Sending new email task with SENT status"""
    email = Email.objects.get(pk=email_pk)
    send_email(email)
