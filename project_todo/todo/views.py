from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from todo.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend

from todo.serializers import CommentCreateSerializer, TaskSerializer
from todo.models import Comment, Task

# Create your views here.
class TaskListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'due_date']
    
    pagination_class = TaskListPagination
    

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwner,]


class CommentCreateView(generics.ListCreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsOwner,]
    
    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class CommentEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsOwner,]
    
    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)