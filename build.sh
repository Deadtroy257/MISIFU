#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install --upgrade pip

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Debug: Verificar la configuración de entorno y directorios
echo "DJANGO_SETTINGS_MODULE is set to: $DJANGO_SETTINGS_MODULE"
echo "Current directory is: $(pwd)"
echo "Contents of the project directory:"
ls -l

# Convert static asset files
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
python manage.py migrate