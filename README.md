# Overview

A simple authentication backend to support Azure App Service "easyauth" authentication.

# Installation

TBD

# Configuration

Add to installed apps.
```py
INSTALLED_APPS = [
    'easy_auth',
    ...
]
```

Add to authentication backends.
```py
AUTHENTICATION_BACKENDS = ['easy_auth.backends.EasyAuthBackend']
```

Add to urls, above `admin.site.urls`. Specify the path that is currently default. For example if `admin.site.urls` has a path `'admin/'`, then use `'admin/login/'`.
```py
urlpatterns = [
    path('login/', include('easy_auth.urls')),
    ...
]
```