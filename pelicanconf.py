#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = './pelican-alchemy/alchemy'

AUTHOR = 'John Tate'
SITENAME = 'John Tate'
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Home', '/'),
#          ('Writing', '/'),
#          ('Contact', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Github', '#'),
          ('LinkedIn', '#'),)

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
