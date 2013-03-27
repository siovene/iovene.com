#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Salvatore Iovene'
SITENAME = u'Salvatore Iovene'
SITETAGLINE = u'Mostly astrophotography and code'
SITEURL = 'http://iovene.com'
SITELOGO = '/images/me.png'
SITEDESCR = u'Hi, I am a software engineer and astrophotographer living in '\
'Espoo, Finland, and working for the Intel Open Source Technology Centre.'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10
THEME = 'iovene.com-theme-alpha'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = ARCHIVES_URL + 'index.html'
