from django.db import models
from users.models import User
from django.utils import timezone

class GeoSearch(models.Model):
	user = models.ForeignKey(User, related_name="searches", on_delete=models.CASCADE)
	geo_from = models.CharField(max_length=30)	 
	geo_to = models.CharField(max_length=30)
	success = models.BooleanField(default=True)
	search_date = models.DateTimeField(default=timezone.now)


