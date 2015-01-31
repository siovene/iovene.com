#!/usr/bin/env python
# -*- coding: utf-8 -*- #
TYPOGRIFY = True
GOOGLE_ANALYTICS_CODE = 'UA-844985-1'

AUTHOR = u'Salvatore Iovene'
SITENAME = u'Salvatore Iovene'
SITETAGLINE = u'Mostly astrophotography and code'
SITEURL = 'http://iovene.com'
SITELOGO = 'images/me.png'
SITEDESCR = u'Hi, I am a software engineer, road cyclist  and astrophotographer living in '\
'Espoo, Finland, and working for the Intel Open Source Technology Centre.'

GITHUB_URL = 'https://github.com/siovene'
LINKEDIN_URL = 'http://lnkd.in/r5w6Mj'
TWITTER_URL = 'https://twitter.com/siovene'
GOOGLE_URL = 'https://plus.google.com/110703431382853324739/'
FLICKR_URL = 'http://flickr.com/photos/siovene'

LICENSE_NAME = 'CC BY-SA 3.0'
LICENSE_URL  = 'http://creativecommons.org/licenses/by-sa/3.0/'

TIMEZONE = 'Europe/Helsinki'
DEFAULT_LANG = u'en'
SUMMARY_MAX_LENGTH = 75

DEFAULT_PAGINATION = 10
THEME = 'lannisport'
STATIC_PATHS = [
    'files',
    'images',
    'cv'
]

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

CONTACT_URL = 'pages/contact/'
