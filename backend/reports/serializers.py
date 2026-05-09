from rest_framework import serializers

class ReportExportserializer(serializers.ModelSerializer):
    report_type = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    department = serializers.CharField(required=False)