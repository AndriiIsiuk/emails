from django.core.mail import EmailMessage


def send_email(mail):
    email_data = dict(
        subject=mail.title,
        body=mail.message,
        from_email=mail.sender,
        to=mail.recipients,
    )

    # TODO make Celery task to send emails
    # celery_send_email_task(email_data)
    mail = EmailMessage(**email_data)
    print(11111111, mail.attachments)

    for file in mail.attachments:
        mail.attach_file(file.attachment.path)

    print(mail)
    mail.send()
