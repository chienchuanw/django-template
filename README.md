# README.md

## Index

- [README.md](#readmemd)
  - [Index](#index)
  - [Account related](#account-related)
    - [If an User instance doesn't have a UserProfile, how to link one?](#if-an-user-instance-doesnt-have-a-userprofile-how-to-link-one)
  - [Parking related](#parking-related)
    - [How to update CSV file automatically using Celery?](#how-to-update-csv-file-automatically-using-celery)
    - [How to import parking data from a CSV with provided API?](#how-to-import-parking-data-from-a-csv-with-provided-api)

## Account related

### If an User instance doesn't have a UserProfile, how to link one?

1. `$ python manage.py create_user_profile` will look all User instance in database and generate UserProfile for those who don't have one.

## Parking related

### How to update CSV file automatically using Celery?

1. `$ make migrate` to migrate `django_celery_beat` into database.
2. `$ python manage.py setup_periodic_task --int <minutes>` to create a scheduled task of updating CSV with given minutes. Default update interval is 3 minutes.
3. `$ make celery-worker` to start celery worker for launch the tasks from tasks.py.
4. `$ make celery-beat` to enable scheduled task which will auto-run the task base on its interval.

Additionally, if you want to change the interval of an existing schedule task:

1. `$ python manage.py update_periodic_task --name <task name> --int <new interval>`

### How to import parking data from a CSV with provided API?

1. Make sure there is CSV file in `data/input`.
2. `$ make migrate`
3. `$ python manage.py import_parkinglots`
