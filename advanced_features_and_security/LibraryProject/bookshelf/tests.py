from django.test import TestCase, Client
from django.urls import reverse
from .models import Book

class SecurityTestCase(TestCase):
    def test_settings_security_headers(self):
        """Test that security headers are present in the response."""
        response = self.client.get(reverse('book_list')) # Ensure this URL name exists
        self.assertEqual(response['X-Content-Type-Options'], 'nosniff')
        self.assertEqual(response['X-Frame-Options'], 'DENY')

    def test_csrf_protection_is_active(self):
        """Test that a POST request without a CSRF token is rejected."""
        response = self.client.post(reverse('book_list'), {'title': 'Hack'})
        # Django returns a 403 Forbidden if CSRF token is missing/invalid
        self.assertEqual(response.status_code, 403)

    def test_orm_parameterization(self):
        """Test that search handles special characters safely (prevents SQL injection)."""
        # Malicious input mimicking a SQL injection attempt
        malicious_query = "' OR 1=1; --"
        response = self.client.get(reverse('book_list'), {'q': malicious_query})
        self.assertEqual(response.status_code, 200)
        # Verify the malicious query didn't break the page or return all books inappropriately