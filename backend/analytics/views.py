from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from attendance.models import Attendance
from performance.models import KPI


# Create your views here.
class PerformanceAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_attendance = Attendance.objects.count()
        present_attendance = Attendance.objects.filter(status='present').count()

        attendance_percentage = (
            (present_attendance/total_attendance) *100
            if total_attendance > 0 else 0
        )

        avg_productivity  = KPI.objects.aggregate(
            Avg('productivity_score')
        )['productivity_score__avg'] or 0

        avg_quality = KPI.objects.aggregate(
            Avg('quality_score')
        )['quality_score__avg'] or 0

        return Response({
            "attendance_percentage": attendance_percentage,
            "avg_productivity_score": avg_productivity,
            "avg_quality_score": avg_quality
        })