#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z -w 1 $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.5
done

echo "PostgreSQL started"

# Миграции
python manage.py migrate --noinput

# Сбор статики
python manage.py collectstatic --noinput

exec "$@"
