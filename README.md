# DjangoAdminTest
```
>>> mkdir djangoadminapp
>>> cd djangoadminapp
>>> python3 -m venv denv
>>> source denv/bin/activate
>>> python --version
>>> pip install django djangorestframework
>>> cd .. (go to the main folder where manage.py is.)
>>> django-admin startproject khaatatest . 
>>> django-admin startapp khaata_admin
>>> ./manage.py migrate
>>> ./manage.py makemigrations khaata_admin
>>> ./manage.py migrate khaata_admin
>>> python manage.py createsuperuser --email admin@example.com --username admin
>>> python manage.py runserver
```
Navigate to https://127.0.0.1:8000/admin
