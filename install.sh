#!/bin/bash

set -e

echo "🚀 Installation begins"


# checking for python3
if ! command -v python3 &> /dev/null
then
    echo "❌ python3 is not installed"
    exit 1
fi

# checking for python3-venv
if ! python3 -m venv --help &> /dev/null
then
    echo "❌ python3-venv is not installed"
    exit 1
fi

# checking for git
if ! command -v git &> /dev/null
then
    echo "❌ git is not installed"
    exit 1
fi


# cloning a repository
if [ -d "URL-Shortening-Service" ]
then
    cd URL-Shortening-Service
    git pull
else
    git clone https://github.com/pdnxhdm/URL-Shortening-Service
    cd URL-Shortening-Service
fi


# creating a virtual environment
python3 -m venv .venv
source .venv/bin/activate


# installing dependencies
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt


# checking for .env
if [ ! -f ".env" ]
then
    echo -e "DB_HOST=\"localhost\"\nDB_PORT=5432\nDB_USER=\"postgres\"\nDB_PASS=\"postgres\"\nDB_NAME=\"url_shortening_service\"" > .env
    echo "⚠️ .env created with default values"
fi


# database migration
if ./.venv/bin/alembic upgrade head &> /dev/null
then
    echo "✅ Installation completed successfully!"
    echo "To start the service, run:"
    echo "source .venv/bin/activate && uvicorn src.main:app --reload"
else
    echo "❌ Migration failed"
    echo "👉 Check your PostgreSQL connection in .env"
    echo "👉 Ensure the database 'url_shortening_service' exists"
    echo "👉 Then run manually: source .venv/bin/activate && alembic upgrade head && uvicorn src.main:app --reload"
fi