from django.test import TestCase
from django.test.utils import override_settings

class GoogleAnalyticsTests(TestCase):
    @override_settings(GA_PROPERTY_ID='UA-123456-7')
    def test_ga_tracking(self):
        response = self.client.get('/')
        self.assertContains(response, "_gaq.push(['_setAccount', 'UA-123456-7']);")

class AdminTests(TestCase):
    def test_admin_login_loads(self):
        self.assertEqual(self.client.get('/admin/login/').status_code, 200)
