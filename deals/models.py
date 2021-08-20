from django.db import models
from users.models import User
from django.utils import timezone

class Order(models.Model):
	user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
	geo_from = models.CharField(max_length=30)
	geo_to = models.CharField(max_length=30)
	pw = models.PositiveSmallIntegerField(null=True)
	ps = models.CharField(max_length=30, default="unknown")
	reward = models.CharField(max_length=30)
	comment = models.TextField(null=True)
	order_created_date = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10)

class FeedbackOrder(models.Model):	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, related_name="order_feedbacks", on_delete=models.CASCADE)
	score = models.PositiveSmallIntegerField()
	comment = models.TextField(null=True)
	date = models.DateTimeField(default=timezone.now)

class Run(models.Model):
	user = models.ForeignKey(User, related_name="runs", on_delete=models.CASCADE)
	geo_from = models.CharField(max_length=30)	 
	geo_to = models.CharField(max_length=30)
	run_date = models.DateTimeField()
	transport = models.CharField(max_length=30, null=True)
	comment = models.TextField(null=True)
	run_created_date = models.DateTimeField(default=timezone.now)
	is_opened = models.BooleanField(default=True)
	status = models.CharField(max_length=10)

class FeedbackRun(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)	
	run = models.ForeignKey(Run, related_name="run_feedbacks", on_delete=models.CASCADE)
	score = models.PositiveSmallIntegerField()
	comment = models.TextField(null=True)
	date = models.DateTimeField(default=timezone.now)

class Deal(models.Model):
	order = models.OneToOneField(Order, on_delete=models.CASCADE)
	run = models.OneToOneField(Run, on_delete=models.CASCADE)
	in_progress = models.BooleanField(default=True)
	status = models.CharField(max_length=10)
	date_opened = models.DateTimeField(default=timezone.now)
	date_closed = models.DateTimeField(null=True)

	
