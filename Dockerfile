FROM python:3.7-slim-buster
ENV LANG C.UTF-8

RUN apt-get -y update && apt-get -y autoremove
RUN pip install pipenv

RUN mkdir /app
WORKDIR /app

RUN apt-get install -y python python-pip python-dev

ADD Pipfile /app/Pipfile
ADD Pipfile.lock /app/Pipfile.lock
RUN pipenv install

# This doesn't affect security, just needs to be set to finish building
ENV DJANGO_SECRET_KEY=dummy

ADD . /app
RUN pipenv run python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["pipenv", "run", "newrelic-admin", "run-program", "gunicorn", "pylinks.wsgi:application", "--timeout", "120", "-b", "0.0.0.0:8000", "--access-logfile", "-"]
