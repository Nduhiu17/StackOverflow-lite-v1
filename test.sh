#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='set-your-secret-key-here'
pytest --cov-report term-missing --cov=app
