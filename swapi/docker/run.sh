#!/usr/bin/env sh

set -x
set -o errexit
set -o nounset

python /app/manage.py migrate --noinput
python /app/manage.py collectstatic --noinput

make -C ../app load_data

python /app/manage.py runserver 0.0.0.0:5000
