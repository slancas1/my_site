#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sophie Lancaster'
SITENAME = u'Sophie Lancaster'
SITEURL = 'http://lancastersophie.com'

PATH = 'content'

TIMEZONE = 'America/Indianapolis'

DEFAULT_LANG = u'en'

SOCIAL = (('github', 'https://github.com/slancas1'),
('linkedin', 'https://www.linkedin.com/in/sophie-lancaster-093156112/'),
('facebook', 'https://www.facebook.com/sophie.lancaster.5?ref=bookmarks'),)

RELATIVE_URLS = True

THEME = "/Users/Sophie/Desktop/Google Drive/Random Projects/Repositories/pelican-themes/subtle"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
PAGE_PATHS = ['pages',]
#path = 'Users/Sophie/Desktop/Google%20Drive/Random%20Projects/PelicanSite/output/pages/'
#path = 'pages/'
MENUITEMS = (
	('Home', 'index.html'),
	('Projects', 'projects.html'),
	('Resume', 'resume.html'),
	('Contact Me', 'contactme.html'),
)
