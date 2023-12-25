from django.db import models
from django.utils import timezone

# Create your models here.

class Commit_visit(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    date = models.DateField(default=timezone.now)
    text_input = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    