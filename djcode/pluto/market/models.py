from django.db import models

# Create your models here.

class Quote(models.Model):
	market = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	code = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	opening = models.CharField(max_length=200)
	maximum = models.CharField(max_length=200)
	minimum = models.CharField(max_length=200)
	close = models.CharField(max_length=200)
	volume = models.BigIntegerField()
	amount = models.CharField(max_length=200)
	time = models.DateTimeField()

	class Meta:
		ordering = ('-time', )
		unique_together = (('market','code','time'),)

	def __unicode__(self):
		return '%s' %self.name


class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
			
		