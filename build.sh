#!/usr/bin/env bash
set -o errexit
python -m venv venv

if [[ "$OSTYPE" == "win32" || "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source venv/Scripts/activate
elif [[ "$OSTYPE" == "darwin"* ]]; then
    source venv/bin/activate
else
    source venv/bin/activate
fi

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fixtures/*.json
python manage.py runserver