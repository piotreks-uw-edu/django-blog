"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.models import User

def create_or_update_superuser():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    if username and password:
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            print(f"Updated password for superuser '{username}'")
        except User.DoesNotExist:
            User.objects.create_superuser(username, email='', password=password)
            print(f"Created new superuser '{username}'")

# Call this function at an appropriate place in your manage.py or wsgi.py
create_or_update_superuser()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
