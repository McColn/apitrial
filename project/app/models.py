from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    reg = models.CharField(max_length=20)

class SMS(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ReceivedSMS(models.Model):
    sms_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Received SMS at {self.created_at}"

    