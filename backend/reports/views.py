from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from attendance.models import Attendance
from performance.models import Goal, KPI

# Create your views here.
class ReportSummaryViews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_employees = Attendance.objects.values('employee').distinct().count()
        total_attendance = Attendance.objects.count()
        total_KPIs = KPI.objects.count()
        total_Goal = Goal.objects.count()

        return Response({
            "total_employees": total_employees,
            "total_attendance": total_attendance,
            "total_KPIs": total_KPIs,
            "total_Goal": total_Goal,
        })


