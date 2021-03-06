# assert warnings are enabled
import warnings
warnings.simplefilter("ignore", Warning)

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
	}
}

INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.sites",
	"push_notifications",
]

SITE_ID = 1
ROOT_URLCONF = "core.urls"

SECRET_KEY = "foobar"

PUSH_NOTIFICATIONS_SETTINGS = {}

import os

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(ROOT_DIR,"testmedia")
