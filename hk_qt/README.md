# Questrade Hackathon

This project is a backend + frontend and is responsible for managing users and communicating with the engine service to get maximum loan value when simulating loans.

## Requirements

- Python 3.11
- Poetry (https://python-poetry.org/)
- PostgreSQL 12+

## How to run

1) Clone this repository

```
git clone ....
cd hackatonQT/hk_qt
```

2) Create the `.env` file by copying the `.env.sample` file

```
cp .env.sample .env
```

Edit .env with the correct Postgres connection URL string.

3) Install dependencies and create database tables

```
poetry install
poetry shell
python manage.py migrate
python manage.py seed
```

4) Start the server

```
poetry shell
task run
```

5) The system is available on `http://localhost:8000` address.