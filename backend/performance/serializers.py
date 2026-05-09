from rest_framework import serializers
from .models import Goal, KPI, PerformanceReview

class GoalSerializer(serializers.ModelSerializer):
    employee_name = serializers.StringRelatedField(source='employee', read_only=True)

    class Meta:
        model = Goal
        fields = [
            'id',
            'employee',
            'employee_name',
            'title',
            'description',
            'target_date',
            'progress',
            'status',
        ]

class KPISerializer(serializers.ModelSerializer):
    employee_name = serializers.StringRelatedField(source='employee', read_only=True)

    class Meta:
        model = KPI
        fields = [
            'id',
            'employee',
            'employee_name',
            'productivity_score',
            'quality_score',
            'project_completion_rate',
            'review_period',
        ]

class PerformanceReviewSerializer(serializers.ModelSerializer):
    employee_name = serializers.StringRelatedField(source='employee', read_only=True)
    reviewer_name = serializers.StringRelatedField(source='reviewer', read_only=True)

    class Meta:
        model= PerformanceReview
        fields = [
            'id',
            'employee',
            'employee_name',
            'reviewer_name',
            'feedback',
            'rating',
            'created_At'
        ]