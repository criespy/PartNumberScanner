"""
WSGI config for part_number_scanner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

path='/var/www/PartNumberScanner/'

from django.core.wsgi import get_wsgi_application

if path not in sys.path:
	sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'part_number_scanner.settings')

application = get_wsgi_application()

