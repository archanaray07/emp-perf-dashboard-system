from django.db import models
from django.conf import settings

# Create your models here.
class Attendance(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('present', 'Present'),('absent','Absent'),('leave','Leave')])