from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('3', 'High'),
        ('2', 'Medium'),
        ('1', 'Low'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=7,
        choices=PRIORITY_CHOICES,
        default='Low'
    )
    due_date = models.DateTimeField(null=True, blank=True, default="MM/DD/YYYY HH:mm")

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
