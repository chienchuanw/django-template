from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


# Create an Celery instance
celery_app = Celery("core")
# Celery will read from Django settings.py and only load the variables with "CELERY_" prefix
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
# Celery searches all task.py automatically without register tasks manually
celery_app.autodiscover_tasks()
