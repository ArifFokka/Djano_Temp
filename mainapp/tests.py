from django.test import SimpleTestCase

class MainAppTest(SimpleTestCase):
    def test_homeview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_aboutview(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)