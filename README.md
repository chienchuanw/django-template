# README.md

## Index

- [README.md](#readmemd)
  - [Index](#index)
  - [Account related](#account-related)
    - [If an User instance doesn't have a UserProfile, how to link one?](#if-an-user-instance-doesnt-have-a-userprofile-how-to-link-one)
  - [Parking related](#parking-related)
    - [How to update CSV file automatically using Celery?](#how-to-update-csv-file-automatically-using-celery)

## Account related

### If an User instance doesn't have a UserProfile, how to link one?

1. `$ python manage.py create_user_profile` will look all User instance in database and generate UserProfile for those who don't have one.

## Parking related

### How to update CSV file automatically using Celery?

1. `$ make migrate` to migrate `django_celery_beat` into database.
2. `$ python manage.py setup_periodic_task --int <minutes>` to create a scheduled task of updating CSV with given minutes. Default update interval is 3 minutes.
3. `$ make celery-worker` to start celery worker for launch the tasks from tasks.py.
4. `$ make celery-beat` to enable scheduled task which will auto-run the task base on its interval.
