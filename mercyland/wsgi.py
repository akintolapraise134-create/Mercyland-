"""
WSGI config for mercyland project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercyland.settings')
application = get_wsgi_application()
