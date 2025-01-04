#!/bin/bash

echo "Esperando a que la base de datos esté lista..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done

echo "Base de datos está lista, continuando..."

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

exec "$@"
