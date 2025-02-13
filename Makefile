server:
	poetry run python manage.py runserver

test:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Error: You must specify an app to test. Usage: make test <app_name>"; \
		exit 1; \
	fi
	@poetry run python manage.py test $(filter-out $@,$(MAKECMDGOALS))

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser

styles:
	npx tailwindcss -i ./src/styles/input.css -o ./static/styles/output.css --watch

shell:
	poetry run python manage.py shell

celery-worker:
	celery -A core worker --loglevel=info 

celery-beat:
	celery -A core beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
