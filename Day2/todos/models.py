from django.db import models
from django.utils import timezone
# Create your models here.
# create TABLE todo (
#     id int AUTO_INCREMENT PRIMARY KEY
#     title VARCHAR(50)
#     description TEXT
#     completed BOOLEAN 
# )

class Todo(models.Model):
    title =  models.CharField(max_length=200)
    description  = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    
