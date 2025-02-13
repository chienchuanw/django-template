from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json, datetime


class Command(BaseCommand):
    help = "Setup scheduled Celery Beat Periodic tasks"

    def add_arguments(self, parser):
        parser.add_argument(
            "--int",
            type=int,
            default=3,
            help="Setup the interval of scheduled task",
        )

    def handle(self, *args, **options):
        # Setup interval
        interval = options["int"]
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=interval,
            period=IntervalSchedule.MINUTES,
        )

        # Create schedule task if it doesn't exist

        task_name = "update_parking_csv"

        if not PeriodicTask.objects.filter(name=task_name).exists():
            PeriodicTask.objects.create(
                interval=schedule,
                name=task_name,
                task="parkings.tasks.update_csv",
                args=json.dumps([]),
                start_time=datetime.datetime.now(),
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully create scheduled task: {task_name}")
            )
            self.stdout.write(
                self.style.SUCCESS(f"Task interval is every {interval} minutes")
            )

        else:
            self.stdout.write(self.style.WARNING("This scheduled task exists already"))
