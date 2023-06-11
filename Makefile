apisrv:
	DJANGO_DEBUG=ON poetry run python manage.py runserver 0.0.0.0:9121

webapp:
	cd frontend ; npm run dev

initial:
	poetry install
	poetry run python manage.py collectstatic
	poetry run python manage.py createsuperuser

