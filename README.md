# Overview

A simple authentication backend to support Azure App Service "easyauth" authentication on top of Django's built-in user authentication system.

### How it works

A user authenticating with a Django app that is already signed in under App Service Authentication will have their email address checked against the app's Users list. If matched, they will be logged in automatically. Otherwise, they will fall back to Django's default login process.

# Installation

Clone this repo and in the root run:
```sh
python setup.py sdist
```

This will create a package under `dist/`.

From your Django project, run:
```sh
python -m pip install --user /path/to/dist/django-easyauth-0.1.tar.gz
```

# Configuration

### Add to installed apps

```py
INSTALLED_APPS = [
    'easy_auth',
    ...
]
```

### Add to authentication backends
```py
AUTHENTICATION_BACKENDS = [
    'easy_auth.backends.EasyAuthBackend',
]
```

### Add the login path to url conf

Specify the path that is the current [login URL](https://docs.djangoproject.com/en/4.0/ref/settings/#login-url). The path must be specified before any projects that might override it (e.g. `admin`).

For example if the login URL is `admin/login/`, then add:

```py
urlpatterns = [
    path('admin/login/', include('easy_auth.urls')),
    ...
]
```

### Override the login template

Optionally, if you want to override the fallback login template, it can be changed in settings:

```py
LOGIN_TEMPLATE = 'path/to/your/login.html'
```