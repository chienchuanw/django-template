from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile


class Command(BaseCommand):
    help = "Create UserProfile for User who yet to have one."

    def add_arguments(self, parser):
        parser.add_argument(
            "--show",
            action="store_true",
            help="Show which User creates UserProfile successfully",
        )

    def handle(self, *args, **options):
        # filter User who doesn't have UserProfile
        users_without_profile = User.objects.filter(profile__isnull=True)

        if not users_without_profile.exists():
            self.stdout.write(self.style.SUCCESS("All User has UserProfile already!"))
            return

        yet_created = len(users_without_profile)

        for user in users_without_profile:
            UserProfile.objects.create(user=user)
            yet_created -= 1
            if options["show"]:
                self.stdout.write(
                    self.style.SUCCESS(f"Create UserProfile for User: {user.username}")
                )

        # check if any User fail to create an UserProfile
        if yet_created != 0:
            self.stdout.write(
                self.style.ERROR(f"There are {yet_created} User don't have UserProfile")
            )

            return

        self.stdout.write(
            self.style.SUCCESS("Successfully create UserProfile for all User")
        )
