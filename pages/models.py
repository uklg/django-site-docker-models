from django.db import models


class Town(models.Model):
    name = models.CharField(max_length=25)


class Customer(models.Model):
    name = models.CharField(max_length=30)
    town = models.ForeignKey(Town,on_delete=models.CASCADE)






    
