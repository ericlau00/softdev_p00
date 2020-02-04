#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/p0/")
sys.path.insert(0,"/var/www/p0/p0/")

import logging
logging.basicConfig(stream=sys.stderr)

from p0 import app as application
