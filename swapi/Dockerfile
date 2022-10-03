FROM python:2.7.18-alpine

ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # config
  DEBUG=False \
  ENV=develop \
  DOMAIN_NAME="localhost" \
  ADDITIONAL_ALLOWED_HOSTS="" \
  HASH_SALT="change-me"

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python-dev musl-dev libmemcached-dev zlib-dev \
#  && apk add gcc libffi-dev python-dev build-base linux-headers postgresql-dev postgresql-contrib pcre-dev bash alpine-sdk jpeg-dev zlib-dev \
  && apk add postgresql-dev \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client \
  && apk add make \
  && pip install pip-tools

RUN apk add libmemcached



#RUN apt-get update && \
#    apt-get install -y \
#    # psycopg2 dependencies
#    gcc libpq-dev python3-dev \
#    # Translations dependencies
#    gettext \
#  && apt-get clean \
#  && rm -rf /var/lib/apt/lists/* \
#  && pip install pip-tools==5.4.0


WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["/app/docker/run.sh"]

