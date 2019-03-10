from django.db import models

# Create your models here.

class level(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
		
class student(models.Model):
	options = (
		('tst1','tst1'),
		('tst2','tst2')
		)

	name = models.CharField(max_length=200)
	mobile = models.IntegerField()
	address = models.CharField(max_length=200)
	selectop = models.CharField(max_length=200,choices=options,null=True,default='tst2')
	levellink = models.ForeignKey(level,on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.name

