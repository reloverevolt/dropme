from django.db import models
from django.utils import timezone

class User(models.Model): 
	tid = models.SmallIntegerField()
	lang = models.CharField(max_length=10, default='ru')
	name = models.CharField(max_length=30, default='anonymous')
	nickname = models.CharField(max_length=30, default='anonymous')
	date_joined = models.DateTimeField(default=timezone.now) 
	karma = models.SmallIntegerField(default=0)
