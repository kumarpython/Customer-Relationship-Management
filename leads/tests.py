from django.test import TestCase
from django.urls import reverse


class StartTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('leads:start'))
        self.assertEqual(response.status_code, 200)
        print (response.content)

# Create your tests here.
