from django.db import models

# Create your models here.

class myapp(models.Model):
	name = models.CharField(max_length=200)
	mobile = models.IntegerField()
	address = models.CharField(max_length=200)

	def __str__(self, arg):
		return self.name
		