# Notes

## Celery

### Using celery to schedule tasks with intervals

If you are using `django_celery_beat` extension for scheduling tasks, instead of entering commands:

`$ celery -A <Celery App Name> beat --loglevel=info`

(which will connect to default scheduler: **celery.beat.PersistentScheduler**)

You should enter commands like this by specifying database scheduler of Django:

`$ celery -A <Celery App Name> beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

For further explanation, read [this](https://stackoverflow.com/questions/46913392/celery-beat-not-picking-up-periodic-tasks)

## Google Maps

### Should Google Maps API be exposed directly on HTML?

For the Google Maps Javascript API v3 the keys **must** be public on your page.

Read [here](https://stackoverflow.com/questions/39625587/how-do-i-securely-use-google-api-keys) to know more.
