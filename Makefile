server:
	poetry run python manage.py runserver

test:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Error: You must specify an app to test. Usage: make test <app_name>"; \
		exit 1; \
	fi
	@poetry run python manage.py test $(filter-out $@,$(MAKECMDGOALS))

%:
	@: