#!/usr/bin/env sh

set -x
set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/pages/template/production-checklist.rst

python /app/manage.py migrate --noinput
python /app/manage.py collectstatic --noinput
#python /app/manage.py compilemessages

# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn starwars.wsgi \
  --reload \
  --workers=4 \
  --bind="0.0.0.0:5000" \
  --chdir='/app' \
  --log-file=- \
  --worker-tmp-dir='/dev/shm'

