from django.db import models

# Create your models here.

class Website(models.Model):
	url = models.CharField(max_length=200, unique=True)
	category = models.SmallIntegerField(default=0)
	is_dynamic = models.BooleanField(default=False)
	updated = models.DateTimeField()

	def __unicode__(self):
		return '%d:%s, last updated:%s' %(self.pk, self.url, self.updated)