from django.test import TestCase
from sign.models import Event, Guest

# Create your tests here.
class ModelTest(TestCase):
	
	def setUp(self):
		Event.objects.create(id=21, name="oneplus 3 event",status=True,limit=2000,address='shenzhen',start_time="2016-08-10 14:30:00")
		Guest.objects.create(id=21,event_id=21,realname='alen',phone='13111113333',email='alen@126.com',sign=False)

	def test_event_models(self):
		result = Event.objects.get(name="oneplus 3 event")
		self.assertEqual(result.address,"shenzhen")
		self.assertTrue(result.status)

	def test_guest_models(self):
		result = Guest.objects.get(phone='13111113333')
		self.assertEqual(result.realname,'alen')
		self.assertFalse(result.sign)