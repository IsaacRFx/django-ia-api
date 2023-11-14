#!/bin/bash

cd /home/appuser/app/api/

python manage.py migrate
python api/chatbot_model/training.py

exec "$@"