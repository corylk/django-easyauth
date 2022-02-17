# Overview

A simple authentication backend to support Azure App Service "easyauth" authentication on top of Django's built-in user authentication system.

### How it works

A user authenticating with a Django app that is already signed in under App Service Authentication will have their email address checked against the app's Users list. If matched, they will be logged in automatically. Otherwise, they will fall back to Django's default login process.

# Installation

TBD

# Configuration

### Add to installed apps.
```py
INSTALLED_APPS = [
    ...
    'easy_auth',
]
```

### Add to authentication backends.
```py
AUTHENTICATION_BACKENDS = [
    'easy_auth.backends.EasyAuthBackend',
]
```

### Add the login path to url conf
Specify the path that is the current [login URL](https://docs.djangoproject.com/en/4.0/ref/settings/#login-url).

For example if the login URL `accounts/login/`, then add:

```py
urlpatterns = [
    path('accounts/login/', include('easy_auth.urls')),
    ...
]
```
