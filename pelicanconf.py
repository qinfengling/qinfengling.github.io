#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'qinfengling'
AUTHOR_EMAIL = u'Fengling.Qin@gmail.com'
SITENAME = u'qinfenging.github.io'
SITEURL = ''

GITHUB_USER = u'qinfengling'
GITHUB_SKIP_FORK = True

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['htmls', 'mds', 'orgs', 'rsts']
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('GitHub', 'http://github.com/qinfengling'),
        ('Twitter', 'http://twitter.com/qinfengling'),)

DEFAULT_PAGINATION = 10

# Menu
MENUITEMS = [('home', "/"),
('category', "/categories.html"),
('tag', "/tags/index.html"),
('about me', "/"),
        ]
# About me
ABOUT_ME = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = u'/Users/mikeqin/Documents/virtualpc/share/CMS/pelican-themes/pelican-bootstrap3'
PLUGIN_PATHS = ['/Users/mikeqin/Documents/virtualpc/share/CMS/pelican-plugins']
PLUGINS = ['org_reader', 'gravatar']

ORG_READER_EMACS_LOCATION = u'/Applications/Emacs.app/Contents/MacOS/Emacs'

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Tag
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_TAGS_ON_SIDEBAR = True

ARTICLE_URL = '{date:%Y}/{date:%-m}/{date:%-d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = TAGS_URL + 'index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = ARCHIVES_URL + 'index.html'
CATEGORY_SAVE_AS = False

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%-m}/index.html'
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

CC_LICENSE = "CC-BY-NC-SA"
