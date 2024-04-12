#!/bin/bash


SUPERUSER_EMAIL=${DJANGO_SUPERUSE_EMAIL:-"seanep94@gmail.com"}


cd /app/

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true