from django.test import TestCase, Client
from django.urls import reverse
from .models import UserModel  # Replace 'your_app' with the actual app name

class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_registration_success(self):
        # Define the POST data for a successful registration
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'firstname': 'Test',
            'lastname': 'User',
            'address': 'Test Address',
            'phone': '1234567890',
            'mailid': 'test@example.com',
        }

        # Simulate a POST request to the userRegistration view
        response = self.client.post('userRegistration', data)

        # Assert that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is registered in the database
        self.assertTrue(UserModel.objects.filter(username='testuser').exists())
