"""
WSGI config for kjc_off_piste_skishop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kjc_off_piste_skishop.settings')

# application = get_wsgi_application()

application = WhiteNoise(
    DjangoWhiteNoise(get_wsgi_application()),
    root=settings.MEDIA_ROOT,
    prefix='/media/',
)
