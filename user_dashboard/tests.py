from django.test import TestCase, Client
from django.urls import reverse

class UserDashboardTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_dashboard_view(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_dashboard/dashboard.html')

    def test_admin_dashboard_view(self):
        url = reverse('admin_dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_dashboard/admin_dashboard.html')
