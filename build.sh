#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install --upgrade pip

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
python manage.py migrate

echo "Contents of the project directory:"
ls -l
ls -ld mediafiles
chmod 755 media
ls -ld mediafiles

# Set the environment variables for the superuser
# export DJANGO_SUPERUSER_USERNAME=admin
# export DJANGO_SUPERUSER_EMAIL=admin@correo.com
# export DJANGO_SUPERUSER_PASSWORD=adminpassword

# # Create the superuser
# python manage.py createsuperuser --noinput