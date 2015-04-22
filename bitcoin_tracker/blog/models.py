#blog/models.py
from django.db import models

class Post(models.Model):
	'blog post in the model'
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __unicode__(self):
		return self.title

