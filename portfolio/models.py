from django.db import models

# Create your models here.

class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio/%Y/%m/%d")
    description = models.CharField(max_length=500)