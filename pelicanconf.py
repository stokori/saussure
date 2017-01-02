#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kazi Toko'
SITENAME = 'Saussure'
SITESUBTITLE = "Kazi's character database"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# We literally do not care about feed generation here
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('', ''))

# Social widget
SOCIAL = (('',''))

DEFAULT_PAGINATION = 10
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = ''

THEME = 'theme'
FORMATTED_FIELDS = []

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['assets']

DIRECT_TEMPLATES = ['index', 'categories', 'tags']
STATIC_PATHS = [
    'images',
    'extra/robots.txt', 
    'extra/favicon.ico' ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
ARTICLE_ORDER_BY = 'basename'

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'

AUTHOR_SAVE_AS = ''

DISPLAY_CATEGORIES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
