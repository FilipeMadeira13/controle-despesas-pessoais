from django.test import SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_check_response_from_home_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)