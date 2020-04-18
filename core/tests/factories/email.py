import factory

from core.models import Email


class EmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Email

    sender = factory.LazyAttribute(lambda o: "%s@example.org" % o)
    recipients = factory.LazyAttribute(lambda o: "%s@example.org" % o)
    title = factory.fuzzy.FuzzyText(length=32)
    message = factory.fuzzy.FuzzyText(length=64)
    status = factory.fuzzy.FuzzyChoice(Email.STATUSES, getter=lambda s: s[0])
    priority = factory.fuzzy.FuzzyChoice(Email.PRIORITY, getter=lambda p: p[0])
