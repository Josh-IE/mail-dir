from __future__ import unicode_literals

from django.db import models

# Create your models here.



class users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
	
	