from rest_framework import serializers
from datetime import date
from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, due_date):
        if due_date < date.today():
            raise serializers.ValidationError('Дата выполнения задачи не может быть в прошлом!')
        return due_date
