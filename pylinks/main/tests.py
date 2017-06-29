from django.test import TestCase

from analytics.models import GoogleAnalytics

class GoogleAnalyticsTests(TestCase):
    def test_ga_tracking(self):
        GoogleAnalytics(site_id=1, web_property_id='12345').save()
        response = self.client.get('/')
        self.assertContains(response, "_gaq.push(['_setAccount', '12345']);")

class AdminTests(TestCase):
    def test_admin_login_loads(self):
        self.assertEqual(self.client.get('/admin/login/').status_code, 200)
