# Make Celery is imported when launching Django
from .celery import celery_app

# List out specific modules that want to be exposed in case other modules leak out
__all__ = ["celery_app"]
