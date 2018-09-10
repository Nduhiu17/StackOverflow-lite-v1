#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='set-this-to-be-your-secret-key'
export JWT_SECRET_KEY='set-this-to-be-your-secret-key'
export DATABASE_URL="postgres://nduhiu:password@localhost:5432/stackoverflow_lite"
python manage.py server
