from django.urls import path
from .views import ReportSummaryViews

urlpatterns = [
    path('summary/', ReportSummaryViews.as_view(),name='report_summary'),
]