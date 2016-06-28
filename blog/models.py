from __future__ import unicode_literals

from django.db import models

# Create your models here.
		

class Blog(models.Model):
	author = models.CharField(max_length=100)
	title = models.CharField(max_length = 200)
	body = models.TextField(max_length = 20000)
	timestamp = models.DateTimeField(auto_now_add=True, null = True)

	def get_absolute_url(self):
		return '/%s/' % self.title
