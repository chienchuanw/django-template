from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    help = "Update the interval of an existing scheduled Celery Beat task"

    def add_arguments(self, parser):
        parser.add_argument(
            "--name",
            type=str,
            required=True,
            help="The name of the task to be updated",
        )

        parser.add_argument(
            "--int",
            type=int,
            required=True,
            help="The new interval in minutes",
        )

    def handle(self, *args, **options):
        task_name = options["name"]
        new_interval = options["int"]

        try:
            task = PeriodicTask.objects.get(name=task_name)

            schedule, created = IntervalSchedule.objects.get_or_create(
                every=new_interval,
                period=IntervalSchedule.MINUTES,
            )

            task.interval = schedule
            task.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully updated task '{task_name}' to {new_interval} minutes"
                )
            )

        except PeriodicTask.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Task '{task_name}' does not exist"))
