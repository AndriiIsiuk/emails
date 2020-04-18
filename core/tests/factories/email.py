import string
from random import choice
from typing import List

import factory

from core.models import Email
from factory.fuzzy import FuzzyText, FuzzyChoice


def email_generator(resolver, size: int = 6, chars=string.ascii_lowercase) -> str:
    name = "".join(choice(chars) for _ in range(size))
    return f"{name}@example.org"


def email_list_generator(resolver, size: int = 3) -> List[str]:
    return [email_generator(resolver) for _ in range(size)]


class EmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Email

    sender = factory.LazyAttribute(email_generator)
    recipients = factory.LazyAttribute(email_list_generator)
    title = FuzzyText(length=32)
    message = FuzzyText(length=64)
    status = FuzzyChoice(Email.STATUSES, getter=lambda s: s[0])
    priority = FuzzyChoice(Email.PRIORITY, getter=lambda p: p[0])
