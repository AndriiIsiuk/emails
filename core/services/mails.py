from django.core.mail import EmailMessage

from core.models import Email


def send_email(mail_instance: Email) -> None:
    email_data = dict(
        subject=mail_instance.title,
        body=mail_instance.message,
        from_email=mail_instance.sender,
        to=mail_instance.recipients,
    )

    mail = EmailMessage(**email_data)

    attachments = mail_instance.attachments.all()

    for file in attachments:
        mail.attach_file(file.attachment.path)

    mail.send()
