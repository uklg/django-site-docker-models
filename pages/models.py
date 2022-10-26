from django.db import models


class Town(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name[:49]


class Customer(models.Model):
    name = models.CharField(max_length=30)
    town = models.ForeignKey(Town,on_delete=models.CASCADE)
    def __str__(self):
        return self.name[:50]


#class Categor


class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name[:50]
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]


class Knowledge(models.Model):
    title = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)
    oscars_toy = models.CharField(max_length=600,default="Oculus Quest 2")
    code = models.TextField(max_length=1000,default=None)
    def __str__(self):
        return self.title[:20]


#class Category(models.Model):
#    name = models.



#    class Meta:
#        ordering = ["horn_length"]
#        verbose_name_plural = "oxen"
