from django.test import TestCase, SimpleTestCase

# Create your tests here.

class Test_home(SimpleTestCase):
	def get_status_home(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)