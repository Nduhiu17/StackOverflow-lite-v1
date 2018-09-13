#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='set-this-to-be-your-secret-key'
export DATABASE_URL="postgres://your_username:your_password@localhost:5432/stackoverflow_lite"
python manage.py server
