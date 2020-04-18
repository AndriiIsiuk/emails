from django.core.mail import EmailMessage


def send_email(mail_instance):
    email_data = dict(
        subject=mail_instance.title,
        body=mail_instance.message,
        from_email=mail_instance.sender,
        to=mail_instance.recipients,
    )

    # TODO make Celery task to send emails
    # celery_send_email_task(email_data)
    mail = EmailMessage(**email_data)

    for file in mail_instance.attachments.all():
        mail.attach_file(file.attachment.path)

    mail.send()
