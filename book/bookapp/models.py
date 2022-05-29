from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	author = models.CharField(max_length=50, null=True, blank=True)
	genre = models.CharField(max_length=50, null=True, blank=True)
	description = models.CharField(max_length=1000, null=True, blank=True)
	

	def __str__(self):
		return f"{self.name}"
		
	def get_absolute_url(self):
		return f"/book/{self.pk}"
