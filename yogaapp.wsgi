#!/usr/bin/python3

import sys
import site
import logging


python_home = '/usr/local/venv/yoga'


## for python3 the method python -m venv does not provide the activate_this.py script
#activate_this = python_home + '/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))


# Add the site-packages directory.
python_version = '.'.join(map(str, sys.version_info[:2]))
site_packages = python_home + '/lib/python%s/site-packages' % python_version
site.addsitedir(site_packages)

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, "/var/www/YogaApp/")

from YogaApp import app as application
application.secret_key = 'saltysecret'