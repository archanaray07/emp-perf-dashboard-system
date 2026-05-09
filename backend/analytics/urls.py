from django.urls import path
from .views import PerformanceAnalyticsView

urlpatterns = [
    path('dashboard/', PerformanceAnalyticsView.as_view(), name='analytics_dashboard'),
]