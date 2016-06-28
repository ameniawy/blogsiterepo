from __future__ import unicode_literals

from django.db import models
from blog.models import Blog

# Create your models here.
class Comment(models.Model):
	post2 = models.ForeignKey(Blog, null = True)
	post = models.CharField(max_length=100)
	comment = models.TextField(max_length=300)
	username = models.CharField(max_length=100)
	blog_id = models.IntegerField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)


	def get_absolute_url(self):
		return '/%s/' % self.post
