#blog/tests.py
from __future__ import absolute_import
from django.test import TestCase
from .models import Post

class PostTests(TestCase):

	def test_str(self):
		my_title = Post(title='This is a basic title for a basic test case')
		self.assertEquals(
			str(my_title), 'This is a basic title for a basic test case',
			)