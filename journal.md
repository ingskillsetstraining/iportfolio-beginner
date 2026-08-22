# Building Portfolio Project Using Django 6.1 - Real World Project: A Master For Beginners

#### Initial commit

        modified:   .gitignore
        modified:   README.md
        new file:   journal.md

## Section 1: Invironment Setup

		Unit 1.1:  Django Intro
		Unit 1.2:  Getting Started with Django
		Unit 1.3:  Creating Virtual Environment
		Unit 1.4:  Installing Django

## Section 2: Django Project

#### Unit 2.1: Initializing a Django Project

        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        modified:   journal.md
        new file:   manage.py

#### Unit 2.2: Running the Django Server

		(venv31361) λ python manage.py runserver
		Watching for file changes with StatReloader
		Performing system checks...

		System check identified no issues (0 silenced).

		You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
		Run 'python manage.py migrate' to apply them.
		August 22, 2026 - 21:39:49
		Django version 6.1, using settings 'config.settings'
		Starting WSGI development server at http://127.0.0.1:8000/
		Quit the server with CTRL-BREAK.

		WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
		For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/
	
#### Unit 2.3: Creating the SQLite3 Database

		Note: By default, once you run Django server, it will create an SQLite3 database.


## Section 3: Django Applications

#### Unit 3.1: Creating a Django Application

        new file:   apps/portfolio/__init__.py
        new file:   apps/portfolio/admin.py
        new file:   apps/portfolio/apps.py
        new file:   apps/portfolio/migrations/__init__.py
        new file:   apps/portfolio/models.py
        new file:   apps/portfolio/tests.py
        new file:   apps/portfolio/views.py
        modified:   journal.md

#### Unit 3.2: Registering a Django Application (Default Method)

        modified:   config/settings.py
        modified:   journal.md

		Note:
		1. Error due to unproper path for the 'apps'
		2. Error will be solved in Unit 3.3

#### Unit 3.3: Registering a Django Application (Custom Method)

        modified:   config/settings.py
        modified:   journal.md

		(venv31361) λ python manage.py check
		System check identified no issues (0 silenced).


## Section 4: Basic Django Components