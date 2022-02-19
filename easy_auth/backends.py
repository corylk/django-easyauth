from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from .helpers import get_aad_user_id


class EasyAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        user_id = get_aad_user_id(request.headers)

        try:
            return User.objects.get(email=user_id)
        except User.DoesNotExist:
            return super().authenticate(request, username, password)
