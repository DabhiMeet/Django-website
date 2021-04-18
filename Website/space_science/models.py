from django.db import models
import datetime
# Create your models here.

class mission(models.Model):
    name = models.CharField(max_length=150)
    date1 = models.DateField(auto_now=False)
    img =  models.ImageField(upload_to='pics')
