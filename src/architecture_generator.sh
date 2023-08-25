#!/bin/bash

mkdir lifers_v0
cd lifers_v0

mkdir -p app/templates
mkdir -p app/static/css
mkdir -p app/static/js
mkdir -p app/static/img

touch app/__init__.py
touch app/routes.py
touch app/models.py
touch config.py
touch run.py