# Youtan Auctions

Youtan backend challenge - Auctions System

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Basic Commands

### Install Docker and Docker Compose

-   Read the docs to install and configure **Docker** and **Docker Compose**:
    https://docs.docker.com/

### Starting up

-   On project folder use this command to build the docker containers:

        $ docker compose -f local.yml build

-   Run the initial migrate to database:

        $ docker compose -f local.yml run --rm django python manage.py migrate

-   Up the containers to access a local application on http://localhost:8000/:

        $ docker compose -f local.yml up

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ docker compose -f local.yml run --rm django python manage.py createsuperuser
