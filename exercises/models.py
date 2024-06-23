from django.db import models
from django.core.validators import MinValueValidator 

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    gif_url = models.CharField(null=True, blank=True)
    muscle_group = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name
    
    # class Meta:
    #     unique_together = ['name', 'muscle_group']