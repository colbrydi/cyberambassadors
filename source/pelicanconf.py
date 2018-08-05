#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dirk Colbry'
SITENAME = "CyberAmbassadors"
SITEURL = '.'
PATH = 'content'

#PLUGIN_PATHS=["./plugins"]
#PLUGINS=['ipynb.markup']
#MARKUP = { 'md', 'ipynb'}

TIMEZONE = 'America/Detroit'

# Following items are often useful when publishing
DISQUS_SITENAME = "DirkColbry"
GOOGLE_ANALYTICS = "UA-121560886-1"

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_HOME   = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Comment following line if you want the default theme
THEME = 'themes/tuxlite_cmse'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

#INDEX_SAVE_AS = 'about.html'
#PAGE_SAVE_AS = 'about2.html'
#PAGE_URL = 'about2.html'

# Provides menu items, which come before pages / categories
MENUITEMS = [('Project Summary',SITEURL+'/pages/summary.html'), ('Time Line',SITEURL+'/pages/timeline.html'),('Contact',SITEURL+'/pages/contact.html')]
