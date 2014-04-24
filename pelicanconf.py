#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Neil Maknarakham'
SITENAME = u'mack - na- ra - come'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# theme
THEME = "/Users/NeilMakn/dev_projects/peli_blog/pelican_themes/pelican-themes/subtle"

# Favorite Reads
LINKS =  (('HackerNews', 'http://news.ycombinator.com/user?id=nmkn'),
          ('DataTau', 'http://www.datatau.com'),
          ('FiveThirtyEight', 'http://fivethirtyeight.com/'),
          ('Thrillist', 'http://www.thrillist.com/'),
          ('Grantland', 'http://grantland.com/'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/NeilMakn'),
          ('Instagram', 'http://instagram.com/neilmakn/'),
          ('Github', 'https://github.com/NeilMakn'))

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
