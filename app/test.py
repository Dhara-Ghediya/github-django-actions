from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import UserModel  

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
        response = self.client.post(reverse('user_register'), data)
        
        # Assert that the response is a JSON response with status code 200
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf-8'), {'success': 'Done!!!'})

        # Assert that the user is registered in the database
        self.assertTrue(UserModel.objects.filter(username='testuser').exists())

        # Assert that a success message is in the messages framework
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Register Successfully Done! Now, You have to login...", messages)
        
        