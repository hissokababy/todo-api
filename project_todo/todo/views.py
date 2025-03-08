from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todo.permissions import IsOwnerOrReadOnly

from todo.serializers import TaskSerializer
from todo.models import Task

# Create your views here.

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly,]
