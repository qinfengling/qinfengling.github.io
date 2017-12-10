#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Qin Fengling'
AUTHOR_EMAIL = u'Fengling.Qin@gmail.com'
SITENAME = u'Qin Fengling'
SITEURL = u'qinfengling.io'

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = u'pelican-themes/pelican-bootstrap3'
PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'org_reader']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Don't generate the following pages
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

ORG_READER_EMACS_LOCATION = u'/usr/local/bin/emacs'

# pelican-bootstrap3 settings
HIDE_SIDEBAR = True
BANNER_SUBTITLE = 'Qin Fengling.'
BANNER_ALL_PAGES = True
