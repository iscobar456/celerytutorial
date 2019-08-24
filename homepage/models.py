from django.db import models

# Create your models here.

class Completion_Record(models.Model):
	start_time = models.DateTimeField(null=True)
	end_time = models.DateTimeField(null=True)