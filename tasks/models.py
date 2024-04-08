from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        ordering = ['-created']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
