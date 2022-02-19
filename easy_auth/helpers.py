from django.conf import settings
import logging

from .options import OPTIONS

logger = logging.getLogger(__name__)


def get_option(key):
    return getattr(settings, key, OPTIONS.get(key))

def get_aad_user_id(headers):
    user_id = headers.get(get_option('USERID_HEADER'))
    logger.info('{}: {}'.format('user_id', user_id))
    return user_id
