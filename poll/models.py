from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Addpoll(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    question=models.CharField(max_length=200,null=False,blank=False)
    first_c=models.CharField(max_length=30,null=False,blank=False)
    second_c=models.CharField(max_length=30,null=False,blank=False)
    third_c=models.CharField(max_length=30,null=False,blank=False)
    fourth_c=models.CharField(max_length=30,null=False,blank=False)
    
    def __str__(self):
        return self.question
