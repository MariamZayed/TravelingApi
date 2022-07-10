#!/bin/sh

apt-get update
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
chown -R "$USER":www-data /static/ && chmod -R 755 /static/
gunicorn Traveling.wsgi:application --bind 0.0.0.0:8000