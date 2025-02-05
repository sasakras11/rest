from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # Add timestamp with default value
    priority = models.IntegerField(choices=[
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High')
    ], default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # One-to-Many
    tags = models.ManyToManyField(Tag)

    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'category', 'tags']

        from rest_framework import serializers

        

