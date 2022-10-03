FROM python:3.8.8-slim

ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # config
  DEBUG=False \
  ENV=develop \
  DOMAIN_NAME="localhost" \
  ADDITIONAL_ALLOWED_HOSTS="" \
  DATABASE_URL=postgres://postgres:postgres@db/starwars \
  HASH_SALT="change-me"

RUN apt-get update && \
    apt-get install -y \
    # psycopg2 dependencies
    gcc libpq-dev python3-dev \
    # Translations dependencies
    gettext \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && pip install pip-tools==5.4.0


WORKDIR /app

COPY requirements.txt /app
RUN pip-sync requirements.txt

COPY . /app

CMD ["/app/docker/run.sh"]

