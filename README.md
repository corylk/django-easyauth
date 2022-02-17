# Overview

A simple authentication backend to support Azure App Service "easyauth" authentication.

# Installation

TBD

# Configuration

Add to installed apps:
```py
INSTALLED_APPS = [
    'easy_auth',
    ...
]
```

Add to authentication backends:
```py
AUTHENTICATION_BACKENDS = ['easy_auth.backends.EasyAuthBackend']
```