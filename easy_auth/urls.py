from django.conf import settings
from django.urls import path

from .views import EasyAuthLoginView


urlpatterns = [
    path('', EasyAuthLoginView.as_view(template_name=getattr(
        settings, 'LOGIN_TEMPLATE', 'admin/login.html')), name="login"),
]
