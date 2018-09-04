#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='set-this-to-be-your-secret-key'
python manage.py server
~                        