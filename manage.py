#!/usr/bin/python
import os,sys
from django.core.management import setup_environ, execute_from_command_line
from django.conf import settings

try:
     import settings as settings_mod # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    setup_environ(settings_mod)
    sys.path.insert(0, os.path.join(settings.PROJECT_ROOT, 'apps'))
    execute_from_command_line()
