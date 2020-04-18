from .base import *

DEBUG = True

ALLOWED_HOSTS += ["0.0.0.0"]  # nosec

MIDDLEWARE += ["querycount.middleware.QueryCountMiddleware"]