from django.test import TestCase
from django.conf import settings

class SettingsTests(TestCase):
    def test_installed_apps(self):
        self.assertIn('api', settings.INSTALLED_APPS)
        self.assertIn('rest_framework', settings.INSTALLED_APPS)

    def test_middleware(self):
        self.assertIn('django.middleware.security.SecurityMiddleware', settings.MIDDLEWARE)
        #python manage.py test api.tests.test_endpoints