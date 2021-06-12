from rest_framework import serializers
from .models import students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ['student_id', 'first_name', 'last_name', 'address', 'gender', 'age']