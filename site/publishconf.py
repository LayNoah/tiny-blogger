# Production settings. GitHub Actions passes the Pages URL via the SITEURL env var,
# so this works both for https://<user>.github.io and https://<user>.github.io/<repo>.
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: E402,F401,F403

SITEURL = os.environ.get('SITEURL', '').rstrip('/')
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
