release: python manage.py migrate
web: newrelic-admin run-program gunicorn pylinks.wsgi:application --timeout 120 --log-file -
