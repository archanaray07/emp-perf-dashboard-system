from django.contrib import admin
from .models import Goal, KPI, PerformanceReview

# Register your models here.
admin.site.register(Goal)
admin.site.register(KPI)
admin.site.register(PerformanceReview)
