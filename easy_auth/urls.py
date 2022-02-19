from django.urls import path

from .helpers import get_option
from .views import EasyAuthLoginView


urlpatterns = [
    path('', EasyAuthLoginView.as_view(
        template_name=get_option('LOGIN_TEMPLATE'),
        redirect_authenticated_user=get_option('REDIRECT_AUTH_USERS')),
        name="login"),
]
