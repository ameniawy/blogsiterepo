from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
	post = models.CharField(max_length=100)
	comment = models.TextField(max_length=300)
	username = models.CharField(max_length=100)

	def get_absolute_url(self):
		return '/%s/' % self.post
