from rest_framework import serializers

class PerformanceAnalytics(serializers.ModelSerializer):
    employee_name = serializers.CharField()
    attendance_percentage = serializers.FloatField()
    avg_kpi_score = serializers.FloatField()
    goal_completion_rate = serializers.FloatField()