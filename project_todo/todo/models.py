from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOISES = {
    'pending': 'Pending',
    'in_progress': 'In Progress',
    'completed': 'Completed'
}

class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи', blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOISES, max_length=150, default='pending', verbose_name='Статус задачи')
    due_date = models.DateField(blank=True, null=True, verbose_name='Срок выполнения задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задачи')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего обновления задачи')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='Автор задачи')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
    