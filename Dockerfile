# syntax=docker/dockerfile:1
# check=skip=SecretsUsedInArgOrEnv

FROM python:3.14.0-alpine3.22
ENV LANG=C.UTF-8

RUN apk add --no-cache curl libpq postgresql-dev 
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

RUN mkdir /app
WORKDIR /app

ADD pyproject.toml /app/pyproject.toml
ADD uv.lock /app/uv.lock
RUN uv sync

ADD . /app
ENV DJANGO_SECRET_KEY=dummy
RUN uv run python manage.py collectstatic --noinput
ENV DJANGO_SECRET_KEY=

EXPOSE 8000
CMD ["uv", "run", "newrelic-admin", "run-program", "gunicorn", "pylinks.wsgi:application", "--timeout", "120", "-b", "0.0.0.0:8000", "--access-logfile", "-"]
