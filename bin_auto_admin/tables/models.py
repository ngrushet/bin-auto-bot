from django.db import models

class File(models.Model):
    file_name   = models.CharField(max_length=255)
    description = models.TextField()
    car_model   = models.TextField()
    file_link   = models.URLField()
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)