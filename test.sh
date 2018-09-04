#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='hii-inafaa-kua-siri'
pytest --cov-report term-missing --cov=app
