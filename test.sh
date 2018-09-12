#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='set-your-secret-key-here'
export DATABASE_URL="postgres://nduhiu:password@localhost:5432/stackoverflow_lite_test"
export JWT_SECRET_KEY='this-is-secret'

pytest --cov-report term-missing --cov=app
