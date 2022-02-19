from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
import logging

from .constants import USERID_HEADER

logger = logging.getLogger(__name__)


class EasyAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        user_id = request.headers.get(getattr(
            settings, 'USERID_HEADER', USERID_HEADER))
        logger.info('{}: {}'.format(USERID_HEADER, user_id))
        try:
            return User.objects.get(email=user_id)
        except User.DoesNotExist:
            return super().authenticate(request, username, password)
