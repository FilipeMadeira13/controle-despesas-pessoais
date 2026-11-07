from django.test import Client, SimpleTestCase

class SimpleTest(SimpleTestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_check_response_from_home_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)