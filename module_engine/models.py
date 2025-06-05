from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_installed = models.BooleanField(default=False)
    version = models.CharField(max_length=20, default='1.0.0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
