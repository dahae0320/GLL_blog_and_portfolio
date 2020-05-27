from django.db import models

# Create your models here.

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/%Y/%M/%D/')
    description = models.CharField(max_length=500)