"""ASGI config for identicons project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'identicons.settings')

application = get_asgi_application()
