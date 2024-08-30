from rest_framework import serializers
from .models import Task 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Specify the model
        fields = '__all__'  # or specify the fields explicitly, e.g., ['id', 'name', 'description']
