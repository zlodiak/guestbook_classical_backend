from django.db import models
from django.utils import timezone

class Message(models.Model):
	name = models.CharField(max_length=40)
	text = models.TextField()
	created_date_unix = models.CharField(max_length=40)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
	   return self.text[0:20]  