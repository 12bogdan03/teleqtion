#!/usr/bin/env python
import os
import sys
from decouple import config

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          config('DJANGO_SETTINGS_MODULE',
                                 default='teleqtion.settings.local'))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    from django.conf import settings
    sys.path.append(os.path.join(settings.BASE_DIR, "apps"))

    execute_from_command_line(sys.argv)
