from django.db import models
from django.conf import settings

# Create your models here.
class Goal(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_date = models.DateField()
    progress = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='pending')

class KPI(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productivity_score = models.FloatField()
    quality_score = models.FloatField()
    project_completion_rate = models.FloatField()
    review_period = models.CharField(max_length=50)

class PerformanceReview(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='reviewer')
    feedback = models.TextField()
    rating = models.IntegerField()
    created_At = models.DateTimeField(auto_now_add=True)
    