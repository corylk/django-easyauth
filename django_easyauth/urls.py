from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('login/', include('easy_auth.urls')),
    path('', admin.site.urls),
]