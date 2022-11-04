Django DRF Blog Api
Table of Contents
Overview
Stack & Tools
Project Structure
How to use
Contact
Overview
This is a back-end blog-api project made with Django DRF. To build this project I have used various tools, including drf-yasg, django toolbar, and django rest auth

Stack & Tools
Django
Django Rest Framework

Project Structure
.──── django-drf-blog-api (repo)
│
.
├── README.md
├── api1
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __pycache__
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── project1
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── db.sqlite3

How To Use
To clone and run this application, you'll need Git

# Clone this repository
$ git clone https://github.com/MSKose/django-drf-blog-api

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Run the app
    $ python manage.py runserver
Contact
Linkedin
GitHub