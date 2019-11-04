from django.db import models

# Create your models here.
class employee(models.Model):
	ename=models.CharField(max_length=30)
	eno=models.IntegerField()
	esal=models.FloatField()
	eaddress=models.CharField(max_length=40)
	def __str__(self):
		return self.ename
