from django.db import models

# Create your models here.
class Agent(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    age = models.IntegerField()
    address = models.CharField(max_length=200)  
    agent_id = models.CharField(max_length=10) 
    mobile = models.CharField(max_length=10)  
  
    def __str__(self):  
        return self.agent_id