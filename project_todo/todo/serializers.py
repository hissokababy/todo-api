from rest_framework import serializers
from datetime import date
from todo.models import Comment, Task

class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'    

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comments = CommentCreateSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'due_date', 'created_at', 
                  'updated_at', 'user', 'comments')

    def validate_due_date(self, due_date):
        if due_date < date.today():
            raise serializers.ValidationError('Дата выполнения задачи не может быть в прошлом!')
        return due_date
    