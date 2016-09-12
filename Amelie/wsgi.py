"""
WSGI config for Emilie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('D:/Program Files/python34/lib/site-packages') #it's key to solve apache problem no module named django leading to cant be import
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Emilie.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
