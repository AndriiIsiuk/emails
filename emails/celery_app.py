import os

from django.conf import settings

from celery import Celery
from environs import Env

env = Env()
env.read_env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("SETTINGS"))

app = Celery("emails")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = (
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"
)
app.autodiscover_tasks(["core"])
