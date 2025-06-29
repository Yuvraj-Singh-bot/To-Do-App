from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class ToDoApp(models.Model) : 
    srno = models.AutoField(auto_created=True,primary_key=True) 
    title = models.CharField(max_length=50) 
    date = models.DateTimeField(auto_now_add=True) # Will Automatically assign the date and time 
    status = models.BooleanField(default=False,blank=True) 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    
    

