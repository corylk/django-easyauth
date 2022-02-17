from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EasyAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        user_id = request.headers.get('X-MS-CLIENT-PRINCIPAL-ID')
        try:
            user = User.objects.get(email=user_id)
        except User.DoesNotExist:
            return super().authenticate(request, username, password)
        return user
