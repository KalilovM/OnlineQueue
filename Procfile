release: python manage.py migrate --run-syncdb
web gunicorn Legacy.wsgi:application --log-file -