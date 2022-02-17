from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EasyAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        user_name = request.headers.get('X-MS-CLIENT-PRINCIPAL-NAME')
        user_id = request.headers.get('X-MS-CLIENT-PRINCIPAL-ID')
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return None
        return user
