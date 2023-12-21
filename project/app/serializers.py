from rest_framework import serializers
from .models import Student,SMS,ReceivedSMS

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','reg']


class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['content', 'timestamp']

class ReceivedSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedSMS
        fields = ['id', 'sms_data', 'created_at']