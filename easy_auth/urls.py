from django.conf import settings
from django.urls import path

from .constants import LOGIN_TEMPLATE
from .views import EasyAuthLoginView


urlpatterns = [
    path('', EasyAuthLoginView.as_view(template_name=getattr(
        settings, 'LOGIN_TEMPLATE', LOGIN_TEMPLATE)), name="login"),
]
