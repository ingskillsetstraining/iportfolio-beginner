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

#### Unit 4.1: Django Views

        modified:   apps/portfolio/views.py
        modified:   journal.md

#### Unit 4.2: Django URLs

        modified:   config/urls.py
        modified:   journal.md

        Note: You should see Halo, Dunia! in the browser.

#### Unit 4.3: Django Templates

        modified:   apps/portfolio/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   journal.md
        new file:   templates/portfolio/index.html

#### Unit 4.4: Serving Static Data

        modified:   apps/portfolio/views.py
        modified:   journal.md
        modified:   templates/portfolio/index.html

#### Unit 4.5: Django Models

		(venv31361) λ python manage.py makemigrations portfolio
		Migrations for 'portfolio':
		  apps\portfolio\migrations\0001_initial.py
		    + Create model KontenHalaman

		D:\devspace\W3SCHOOLS-LEARN-FROM\DJANGO\iPortfolio-project(main -> origin)
		(venv31361) λ python manage.py migrate
		Operations to perform:
		  Apply all migrations: admin, auth, contenttypes, portfolio, sessions
		Running migrations:
		  Applying contenttypes.0001_initial... OK
		  Applying auth.0001_initial... OK
		  Applying admin.0001_initial... OK
		  Applying admin.0002_logentry_remove_auto_add... OK
		  Applying admin.0003_logentry_add_action_flag_choices... OK
		  Applying contenttypes.0002_remove_content_type_name... OK
		  Applying auth.0002_alter_permission_name_max_length... OK
		  Applying auth.0003_alter_user_email_max_length... OK
		  Applying auth.0004_alter_user_username_opts... OK
		  Applying auth.0005_alter_user_last_login_null... OK
		  Applying auth.0006_require_contenttypes_0002... OK
		  Applying auth.0007_alter_validators_add_error_messages... OK
		  Applying auth.0008_alter_user_username_max_length... OK
		  Applying auth.0009_alter_user_last_name_max_length... OK
		  Applying auth.0010_alter_group_name_max_length... OK
		  Applying auth.0011_update_proxy_permissions... OK
		  Applying auth.0012_alter_user_first_name_max_length... OK
		  Applying portfolio.0001_initial... OK
		  Applying sessions.0001_initial... OK

        new file:   apps/portfolio/migrations/0001_initial.py
        modified:   apps/portfolio/models.py
        modified:   journal.md


## Section 5: Django CRUD

#### Unit 5.1: Inserting Data

		(venv31361) λ python manage.py shell
		13 objects imported automatically (use -v 2 for details).

		Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
		Type "help", "copyright", "credits" or "license" for more information.
		(InteractiveConsole)
		>>> 
		>>> KontenHalaman.objects.create(judul="Selamat Datang di iPortfolio!", sub_judul="Halaman ini dipanggil menggunakan struktur templates global.")
		<KontenHalaman: KontenHalaman object (1)>

#### Unit 5.2: Updating Data

		>>> data = KontenHalaman.objects.get(id=1)
		>>> data.judul
		'Selamat Datang di iPortfolio!'
		>>> data.sub_judul
		'Halaman ini dipanggil menggunakan struktur templates global.'
		>>> data.sub_judul = "Halaman ini dipanggil secara dinamis menggunakan Django ORM dan Context."
		>>> data.save()
		>>> data.sub_judul
		'Halaman ini dipanggil secara dinamis menggunakan Django ORM dan Context.'
		>>>

#### Unit 5.3: Reading Data

		>>> semua_data = KontenHalaman.objects.all()
		>>> semua_data
		<QuerySet [<KontenHalaman: KontenHalaman object (1)>]>
		>>>
		>>> data_tunggal = KontenHalaman.objects.get(id=1)
		>>> data_tunggal
		<KontenHalaman: KontenHalaman object (1)>
		>>>
		>>> data_tunggal.judul
		'Selamat Datang di iPortfolio!'
		>>>
		>>> data_tunggal.sub_judul
		'Halaman ini dipanggil secara dinamis menggunakan Django ORM dan Context.'
		>>>

#### Unit 5.4: Creating a Superuser

        modified:   journal.md

		(venv31361) λ python manage.py createsuperuser
		Username (leave blank to use 'asus'): c
		Email address: superuser@mail.com
		Password:
		Password (again):
		The password is too similar to the email address.
		Bypass password validation and create user anyway? [y/N]: y
		Superuser created successfully.

#### Unit 5.5: Deleting Data

		(venv31361) λ python manage.py shell
		13 objects imported automatically (use -v 2 for details).

		Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
		Type "help", "copyright", "credits" or "license" for more information.
		(InteractiveConsole)
		>>>
		>>> # Create new object
		>>> KontenHalaman.objects.create(judul="Data Uji Coba", sub_judul="Teks ini sengaja dibuat untuk eksperimen penghapusan.")
		<KontenHalaman: KontenHalaman object (2)>
		>>>
		>>> # Delete an object
		>>> target = KontenHalaman.objects.get(id=2)
		>>> target.delete()
		(1, {'portfolio.KontenHalaman': 1})

		>>> # Check the result
		>>> KontenHalaman.objects.all()
		<QuerySet [<KontenHalaman: KontenHalaman object (1)>]>

#### Unit 5.6: Updating Models

		modified:   apps/portfolio/models.py


## Section 6: Creating Web Pages

#### Unit 6.1: Creating the Home Page

        new file:   apps/portfolio/urls.py
        modified:   apps/portfolio/views.py
        modified:   config/urls.py
        modified:   journal.md
        new file:   templates/portfolio/home.html
        deleted:    templates/portfolio/index.html