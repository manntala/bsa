#!/bin/sh

# Wait for PostgreSQL to be ready
wait-for-it postgres:5432 --timeout=60 --strict -- echo "Postgres is up"

# Run migrations (optional)
python manage.py migrate

# Start the server
exec "$@"
