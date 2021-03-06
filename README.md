# Overview

A simple authentication backend to support Azure App Service "easyauth" authentication on top of Django's built-in user authentication system.

### How it works

A user authenticating with a Django app that is already signed in under App Service Authentication will have their email address checked against the app's Users list. If matched, they will be logged in automatically. Otherwise, they will fall back to Django's default login process.

# Installation

From your Django project, run:
```sh
wget https://github.com/corylk/django-easyauth/releases/download/v0.1/django-easyauth-0.1.tar.gz
python -m pip install --user django-easyauth-0.1.tar.gz
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

Specify the path that is the current [login URL](https://docs.djangoproject.com/en/4.0/ref/settings/#login-url) to ensure that unauthenticated users are redirected to the right view. The path must be specified before any projects that might override it (e.g. `admin`).

For example if the login URL is `admin/login/`, then add:

```py
urlpatterns = [
    path('admin/login/', include('easy_auth.urls')),
    ...
]
```

## Optional configuration

### Change the header used to access the user ID

By default, the user ID (email) is expected in the `X-MS-CLIENT-PRINCIPAL-NAME` header provided by App Service ([read more](https://docs.microsoft.com/en-us/azure/app-service/configure-authentication-user-identities)). To change which claim is used, specify a different header with `USERID_HEADER`:

```py
USERID_HEADER = 'x-ms-some-other-header'
```

The header name is case insensitive.

### Redirect authenticated users that access login

By default, authenticated users will still be able to access the Django login form if accessed directly. This behavior can be changed with `REDIRECT_AUTH_USERS`, along with `LOGIN_REDIRECT_URL`.

Before enabling this feature, read more about the risks of doing this [here](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.views.LoginView.redirect_authenticated_user).

```py
REDIRECT_AUTH_USERS = True
LOGIN_REDIRECT_URL = '/admin'
```

### Override the login template

If you want to override the template of the fallback login form, the template path can be changed with `LOGIN_TEMPLATE`:

```py
LOGIN_TEMPLATE = 'path/to/your/login.html'
```
